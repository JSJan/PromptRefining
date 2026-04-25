import tiktoken

from app.core.pricing import MODEL_PROVIDERS, OPENAI_ENCODINGS


def count_tokens(text: str, model: str) -> int:
    """Count tokens for a given text and model."""
    provider = MODEL_PROVIDERS.get(model)

    if provider == "openai":
        return _count_openai_tokens(text, model)
    elif provider == "anthropic":
        return _count_anthropic_tokens(text)
    else:
        raise ValueError(f"Unsupported model: {model}")


def _count_openai_tokens(text: str, model: str) -> int:
    """Count tokens using tiktoken for OpenAI models."""
    encoding_name = OPENAI_ENCODINGS.get(model, "cl100k_base")
    encoding = tiktoken.get_encoding(encoding_name)
    return len(encoding.encode(text))


def _count_anthropic_tokens(text: str) -> int:
    """Estimate tokens for Anthropic models.

    Anthropic doesn't provide an official tokenizer library.
    Using tiktoken cl100k_base as a reasonable approximation.
    For production use, consider using Anthropic's count_tokens API.
    """
    encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))
