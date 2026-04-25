from pydantic import BaseModel


class TokenCount(BaseModel):
    model: str
    provider: str
    token_count: int
    cost_input_per_1k: float
    cost_output_per_1k: float
    estimated_input_cost: float
    estimated_output_cost: float


class AnalyzeResponse(BaseModel):
    prompt: str
    character_count: int
    word_count: int
    token_counts: list[TokenCount]


class RefinedPrompt(BaseModel):
    model_config = {"protected_namespaces": ()}

    original_prompt: str
    refined_prompt: str
    refinement_style: str
    provider_used: str
    model_used: str
    original_analysis: AnalyzeResponse
    refined_analysis: AnalyzeResponse
    token_savings: dict[str, int]
    cost_savings: dict[str, float]


class ModelInfo(BaseModel):
    name: str
    provider: str
    input_price_per_1m: float
    output_price_per_1m: float


class ModelsResponse(BaseModel):
    models: list[ModelInfo]
