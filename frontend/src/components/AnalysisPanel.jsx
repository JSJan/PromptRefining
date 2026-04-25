import { formatCost } from "../utils/formatters";

export default function AnalysisPanel({ analysis }) {
  return (
    <div className="bg-white rounded-lg border border-gray-200 p-4">
      <h2 className="text-lg font-semibold text-gray-800 mb-3">
        Token Analysis
      </h2>
      <div className="text-sm text-gray-500 mb-3">
        {analysis.character_count} chars · {analysis.word_count} words
      </div>
      <div className="space-y-3">
        {analysis.token_counts.map((tc) => (
          <div
            key={tc.model}
            className="border border-gray-100 rounded p-3 bg-gray-50"
          >
            <div className="flex justify-between items-center">
              <span className="font-medium text-sm text-gray-700">
                {tc.model}
              </span>
              <span className="text-xs text-gray-400 uppercase">
                {tc.provider}
              </span>
            </div>
            <div className="mt-1 text-2xl font-bold text-gray-900">
              {tc.token_count.toLocaleString()}
              <span className="text-sm font-normal text-gray-400 ml-1">
                tokens
              </span>
            </div>
            <div className="mt-1 text-xs text-gray-500">
              Input: {formatCost(tc.estimated_input_cost)} · Output:{" "}
              {formatCost(tc.estimated_output_cost)}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
