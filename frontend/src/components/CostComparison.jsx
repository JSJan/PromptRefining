import { formatCost } from "../utils/formatters";

export default function CostComparison({ refinement }) {
  const savings = refinement.token_savings;
  const costSavings = refinement.cost_savings;

  return (
    <div className="bg-white rounded-lg border border-gray-200 p-4">
      <h2 className="text-lg font-semibold text-gray-800 mb-3">
        Savings Comparison
      </h2>
      <div className="space-y-2">
        {Object.entries(savings).map(([model, tokenDiff]) => (
          <div
            key={model}
            className="flex justify-between items-center text-sm border-b border-gray-100 pb-2"
          >
            <span className="text-gray-600">{model}</span>
            <div className="text-right">
              <span
                className={
                  tokenDiff > 0 ? "text-green-600" : "text-red-600"
                }
              >
                {tokenDiff > 0 ? "−" : "+"}
                {Math.abs(tokenDiff)} tokens
              </span>
              <span className="text-gray-400 ml-2">
                ({formatCost(Math.abs(costSavings[model]))}{" "}
                {costSavings[model] >= 0 ? "saved" : "added"})
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
