from openai import AsyncOpenAI
from anthropic import AsyncAnthropic

from app.core.config import settings, GITHUB_MODELS_BASE_URL

REFINEMENT_SYSTEM_PROMPT = """You are an expert prompt engineer. Your task is to refine and improve the user's prompt.

Guidelines for refinement:
1. Make the prompt clearer and more specific
2. Add structure (numbered steps, sections) where helpful
3. Remove ambiguity and vague language
4. Preserve the original intent completely
5. Optimize for fewer tokens where possible without losing meaning
6. Add relevant constraints or output format instructions if missing

Style: {style}

Respond with ONLY the refined prompt. Do not include explanations, preamble, or meta-commentary."""

STYLE_INSTRUCTIONS = {
    "concise": "Minimize token usage aggressively. Strip all unnecessary words. Be direct and terse.",
    "balanced": "Balance clarity with brevity. Use natural language but eliminate redundancy.",
    "detailed": "Prioritize completeness and clarity. Add context and examples if they improve the prompt.",
    "structured": "Reorganize into clear sections with headers, numbered steps, and explicit output format.",
}


async def refine_prompt(
    prompt: str,
    provider: str = "openai",
    model: str | None = None,
    style: str = "balanced",
) -> tuple[str, str, str]:
    """Refine a prompt using the specified LLM provider.

    Returns:
        Tuple of (refined_prompt, provider_used, model_used)
    """
    style_instruction = STYLE_INSTRUCTIONS.get(style, STYLE_INSTRUCTIONS["balanced"])
    system_prompt = REFINEMENT_SYSTEM_PROMPT.format(style=style_instruction)

    if provider == "openai":
        return await _refine_with_openai(prompt, system_prompt, model)
    elif provider == "anthropic":
        return await _refine_with_anthropic(prompt, system_prompt, model)
    else:
        raise ValueError(f"Unsupported provider: {provider}")


async def _refine_with_openai(
    prompt: str, system_prompt: str, model: str | None
) -> tuple[str, str, str]:
    model = model or "gpt-4o"

    # Use direct OpenAI key if available, otherwise fall back to GitHub token
    if settings.openai_api_key:
        client = AsyncOpenAI(api_key=settings.openai_api_key)
        api_model = model
    elif settings.github_token:
        client = AsyncOpenAI(
            api_key=settings.github_token,
            base_url=GITHUB_MODELS_BASE_URL,
        )
        # GitHub Models requires provider prefix (e.g. "openai/gpt-4o")
        api_model = f"openai/{model}" if "/" not in model else model
    else:
        raise ValueError("No OpenAI API key or GitHub token configured")

    response = await client.chat.completions.create(
        model=api_model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        temperature=0.3,
    )

    refined = response.choices[0].message.content.strip()
    provider_label = "openai" if settings.openai_api_key else "github-models"
    return refined, provider_label, model


async def _refine_with_anthropic(
    prompt: str, system_prompt: str, model: str | None
) -> tuple[str, str, str]:
    model = model or "claude-3-5-sonnet-20241022"
    client = AsyncAnthropic(api_key=settings.anthropic_api_key)

    response = await client.messages.create(
        model=model,
        max_tokens=4096,
        system=system_prompt,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    refined = response.content[0].text.strip()
    return refined, "anthropic", model
