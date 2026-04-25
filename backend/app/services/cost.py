from app.core.pricing import MODEL_PRICING


def calculate_cost(token_count: int, model: str, direction: str = "input") -> float:
    """Calculate cost in USD for a given token count and model.

    Args:
        token_count: Number of tokens.
        model: Model name (e.g., 'gpt-4o').
        direction: 'input' or 'output'.

    Returns:
        Cost in USD.
    """
    pricing = MODEL_PRICING.get(model)
    if not pricing:
        raise ValueError(f"No pricing data for model: {model}")

    price_per_1m = pricing[direction]
    return (token_count / 1_000_000) * price_per_1m


def calculate_cost_per_1k(model: str, direction: str = "input") -> float:
    """Get the cost per 1,000 tokens for display purposes."""
    pricing = MODEL_PRICING.get(model)
    if not pricing:
        raise ValueError(f"No pricing data for model: {model}")

    return pricing[direction] / 1000
