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


class MissingElement(BaseModel):
    element: str
    impact: str
    explanation: str


class Improvement(BaseModel):
    category: str
    before: str
    after: str
    why: str


class QualityScore(BaseModel):
    original: int
    refined: int


class PromptQualityBreakdown(BaseModel):
    clarity: QualityScore
    specificity: QualityScore
    structure: QualityScore
    token_efficiency: QualityScore
    completeness: QualityScore


class CliCommand(BaseModel):
    command: str
    description: str
    example: str


class CliTips(BaseModel):
    claude_cli: list[CliCommand]
    copilot_cli: list[CliCommand]
    general_tips: list[str]


class ComparisonAnalysis(BaseModel):
    score_original: int
    score_refined: int
    missing_elements: list[MissingElement]
    improvements_made: list[Improvement]
    prompt_quality_breakdown: PromptQualityBreakdown
    cli_tips: CliTips


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
    comparison: ComparisonAnalysis | None = None


class ModelInfo(BaseModel):
    name: str
    provider: str
    input_price_per_1m: float
    output_price_per_1m: float


class ModelsResponse(BaseModel):
    models: list[ModelInfo]
