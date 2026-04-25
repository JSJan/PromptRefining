from pydantic import field_validator
from pydantic_settings import BaseSettings


GITHUB_MODELS_BASE_URL = "https://models.github.ai/inference"


class Settings(BaseSettings):
    openai_api_key: str = ""
    anthropic_api_key: str = ""
    github_token: str = ""
    backend_port: int = 8000
    cors_origins: str = "http://localhost:5173"
    default_refinement_provider: str = "openai"
    default_refinement_model: str = "gpt-4o"

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}

    @field_validator("cors_origins", mode="before")
    @classmethod
    def parse_cors_origins(cls, v: str) -> str:
        return v

    @property
    def cors_origins_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",")]


settings = Settings()
