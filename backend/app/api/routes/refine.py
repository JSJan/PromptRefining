from fastapi import APIRouter, HTTPException

from app.models.request import RefineRequest
from app.models.response import RefinedPrompt, AnalyzeResponse, TokenCount, ComparisonAnalysis
from app.services.refiner import refine_prompt
from app.services.comparator import analyze_comparison
from app.services.tokenizer import count_tokens
from app.services.cost import calculate_cost, calculate_cost_per_1k
from app.core.pricing import MODEL_PRICING, MODEL_PROVIDERS
from app.core.config import settings

router = APIRouter()


def _build_analysis(prompt: str) -> AnalyzeResponse:
    """Build analysis for a prompt across all models."""
    token_counts = []
    for model, pricing in MODEL_PRICING.items():
        tokens = count_tokens(prompt, model)
        token_counts.append(
            TokenCount(
                model=model,
                provider=MODEL_PROVIDERS[model],
                token_count=tokens,
                cost_input_per_1k=calculate_cost_per_1k(model, "input"),
                cost_output_per_1k=calculate_cost_per_1k(model, "output"),
                estimated_input_cost=calculate_cost(tokens, model, "input"),
                estimated_output_cost=calculate_cost(tokens, model, "output"),
            )
        )

    return AnalyzeResponse(
        prompt=prompt,
        character_count=len(prompt),
        word_count=len(prompt.split()),
        token_counts=token_counts,
    )


@router.post("/refine", response_model=RefinedPrompt)
async def refine_user_prompt(request: RefineRequest):
    """Refine a prompt and return comparison analysis."""
    provider = request.provider
    model = request.model

    # Validate provider has API key configured
    if provider == "openai" and not settings.openai_api_key and not settings.github_token:
        raise HTTPException(status_code=400, detail="OpenAI API key or GitHub token not configured")
    if provider == "anthropic" and not settings.anthropic_api_key:
        raise HTTPException(status_code=400, detail="Anthropic API key not configured")

    try:
        refined_text, provider_used, model_used = await refine_prompt(
            prompt=request.prompt,
            provider=provider,
            model=model,
            style=request.refinement_style,
        )
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"LLM refinement failed: {str(e)}")

    original_analysis = _build_analysis(request.prompt)
    refined_analysis = _build_analysis(refined_text)

    # Calculate savings per model
    token_savings = {}
    cost_savings = {}
    for orig, ref in zip(original_analysis.token_counts, refined_analysis.token_counts):
        token_savings[orig.model] = orig.token_count - ref.token_count
        cost_savings[orig.model] = round(
            orig.estimated_input_cost - ref.estimated_input_cost, 8
        )

    # Generate detailed comparison analysis
    comparison = None
    try:
        comparison_data = await analyze_comparison(
            original=request.prompt,
            refined=refined_text,
            provider=provider_used if provider_used != "github-models" else "openai",
            model=model_used,
        )
        comparison = ComparisonAnalysis(**comparison_data)
    except Exception:
        pass  # Comparison is optional — don't fail the whole request

    return RefinedPrompt(
        original_prompt=request.prompt,
        refined_prompt=refined_text,
        refinement_style=request.refinement_style,
        provider_used=provider_used,
        model_used=model_used,
        original_analysis=original_analysis,
        refined_analysis=refined_analysis,
        token_savings=token_savings,
        cost_savings=cost_savings,
        comparison=comparison,
    )
