from pydantic import BaseModel, Field


class AnalyzeRequest(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=100000, description="The prompt text to analyze")
    models: list[str] | None = Field(
        default=None,
        description="List of model names to analyze for. If None, analyzes for all supported models.",
    )


class RefineRequest(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=100000, description="The prompt text to refine")
    provider: str = Field(default="openai", description="LLM provider to use for refinement: 'openai' or 'anthropic'")
    model: str | None = Field(default=None, description="Specific model to use. Defaults to provider's best model.")
    refinement_style: str = Field(
        default="balanced",
        description="Refinement approach: 'concise', 'balanced', 'detailed', or 'structured'",
    )
