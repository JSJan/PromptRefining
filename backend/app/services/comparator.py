from openai import AsyncOpenAI
from anthropic import AsyncAnthropic

from app.core.config import settings, GITHUB_MODELS_BASE_URL

COMPARISON_SYSTEM_PROMPT = """You are an expert prompt engineer and analyst. Given an ORIGINAL prompt and a REFINED prompt, produce a detailed comparison analysis.

Return your analysis as valid JSON with exactly this structure (no markdown fencing, no extra text):
{
  "score_original": <1-10>,
  "score_refined": <1-10>,
  "missing_elements": [
    {"element": "<what is missing>", "impact": "high|medium|low", "explanation": "<why it matters>"}
  ],
  "improvements_made": [
    {"category": "<category>", "before": "<original text or pattern>", "after": "<refined text or pattern>", "why": "<explanation>"}
  ],
  "prompt_quality_breakdown": {
    "clarity": {"original": <1-10>, "refined": <1-10>},
    "specificity": {"original": <1-10>, "refined": <1-10>},
    "structure": {"original": <1-10>, "refined": <1-10>},
    "token_efficiency": {"original": <1-10>, "refined": <1-10>},
    "completeness": {"original": <1-10>, "refined": <1-10>}
  },
  "cli_tips": {
    "claude_cli": [
      {"command": "<command or flag>", "description": "<what it does>", "example": "<usage example>"}
    ],
    "copilot_cli": [
      {"command": "<command or flag>", "description": "<what it does>", "example": "<usage example>"}
    ],
    "general_tips": ["<tip 1>", "<tip 2>"]
  }
}

For the CLI tips section:
- **Claude CLI (claude)**: Include relevant commands like `claude --print`, `claude --output-format`, `claude --model`, `claude --system-prompt`, `claude --continue`, `claude --resume`, `claude --allowedTools`, `claude --max-turns`, `/clear`, `/compact`, `/model`, `/memory`, `CLAUDE.md` conventions, and slash commands.
- **GitHub Copilot CLI (gh copilot)**: Include commands like `gh copilot suggest`, `gh copilot explain`, inline chat (`Ctrl+I`), `@workspace`, `#file`, `#selection`, `/fix`, `/tests`, `/explain`, `/doc`, agent mode, and relevant VS Code keybindings.
- Tailor the CLI tips to the specific prompt being analyzed — suggest which commands/flags would work best for THIS particular task.

Return ONLY the JSON object. No markdown code fences, no explanation."""


async def analyze_comparison(
    original: str,
    refined: str,
    provider: str = "openai",
    model: str | None = None,
) -> dict:
    """Generate a detailed comparison between original and refined prompts."""
    user_message = f"""ORIGINAL PROMPT:
{original}

REFINED PROMPT:
{refined}

Analyze the differences and provide the comparison JSON."""

    if provider == "openai" or provider == "github-models":
        return await _compare_with_openai(user_message, model)
    elif provider == "anthropic":
        return await _compare_with_anthropic(user_message, model)
    else:
        raise ValueError(f"Unsupported provider: {provider}")


async def _compare_with_openai(user_message: str, model: str | None) -> dict:
    import json

    model = model or "gpt-4o"

    if settings.openai_api_key:
        client = AsyncOpenAI(api_key=settings.openai_api_key)
        api_model = model
    elif settings.github_token:
        client = AsyncOpenAI(
            api_key=settings.github_token,
            base_url=GITHUB_MODELS_BASE_URL,
        )
        api_model = f"openai/{model}" if "/" not in model else model
    else:
        raise ValueError("No OpenAI API key or GitHub token configured")

    response = await client.chat.completions.create(
        model=api_model,
        messages=[
            {"role": "system", "content": COMPARISON_SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
        temperature=0.2,
    )

    raw = response.choices[0].message.content.strip()
    # Strip markdown fencing if present
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1] if "\n" in raw else raw[3:]
        if raw.endswith("```"):
            raw = raw[:-3]
        raw = raw.strip()

    return json.loads(raw)


async def _compare_with_anthropic(user_message: str, model: str | None) -> dict:
    import json

    model = model or "claude-3-5-sonnet-20241022"
    client = AsyncAnthropic(api_key=settings.anthropic_api_key)

    response = await client.messages.create(
        model=model,
        max_tokens=4096,
        system=COMPARISON_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_message}],
        temperature=0.2,
    )

    raw = response.content[0].text.strip()
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1] if "\n" in raw else raw[3:]
        if raw.endswith("```"):
            raw = raw[:-3]
        raw = raw.strip()

    return json.loads(raw)
