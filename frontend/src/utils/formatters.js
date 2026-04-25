/**
 * Format a cost value in USD with appropriate precision.
 */
export function formatCost(cost) {
  if (cost < 0.0001) {
    return `$${cost.toFixed(8)}`;
  }
  if (cost < 0.01) {
    return `$${cost.toFixed(6)}`;
  }
  return `$${cost.toFixed(4)}`;
}

/**
 * Format a token count with commas.
 */
export function formatTokens(count) {
  return count.toLocaleString();
}
