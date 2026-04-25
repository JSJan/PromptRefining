from fastapi import APIRouter, HTTPException

from app.models.request import AnalyzeRequest
from app.models.response import AnalyzeResponse, TokenCount, ModelInfo, ModelsResponse
from app.services.tokenizer import count_tokens
from app.services.cost import calculate_cost, calculate_cost_per_1k
from app.core.pricing import MODEL_PRICING, MODEL_PROVIDERS

router = APIRouter()


@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze_prompt(request: AnalyzeRequest):
    """Analyze a prompt for token counts and costs across models."""
    models = request.models or list(MODEL_PRICING.keys())

    token_counts = []
    for model in models:
        if model not in MODEL_PRICING:
            raise HTTPException(status_code=400, detail=f"Unsupported model: {model}")

        tokens = count_tokens(request.prompt, model)
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
        prompt=request.prompt,
        character_count=len(request.prompt),
        word_count=len(request.prompt.split()),
        token_counts=token_counts,
    )


@router.get("/models", response_model=ModelsResponse)
async def list_models():
    """List all supported models with pricing information."""
    models = [
        ModelInfo(
            name=name,
            provider=MODEL_PROVIDERS[name],
            input_price_per_1m=pricing["input"],
            output_price_per_1m=pricing["output"],
        )
        for name, pricing in MODEL_PRICING.items()
    ]
    return ModelsResponse(models=models)
