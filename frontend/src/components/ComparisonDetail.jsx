export default function ComparisonDetail({ comparison }) {
  if (!comparison) return null;

  const { score_original, score_refined, missing_elements, improvements_made, prompt_quality_breakdown } = comparison;

  const qualityKeys = [
    { key: "clarity", label: "Clarity" },
    { key: "specificity", label: "Specificity" },
    { key: "structure", label: "Structure" },
    { key: "token_efficiency", label: "Token Efficiency" },
    { key: "completeness", label: "Completeness" },
  ];

  return (
    <div className="space-y-4">
      {/* Overall Scores */}
      <div className="bg-white rounded-lg border border-gray-200 p-4">
        <h2 className="text-lg font-semibold text-gray-800 mb-3">Prompt Score</h2>
        <div className="flex gap-6 justify-center">
          <div className="text-center">
            <div className="text-3xl font-bold text-red-500">{score_original}<span className="text-sm text-gray-400">/10</span></div>
            <div className="text-xs text-gray-500 mt-1">Original</div>
          </div>
          <div className="text-2xl text-gray-300 self-center">→</div>
          <div className="text-center">
            <div className="text-3xl font-bold text-green-600">{score_refined}<span className="text-sm text-gray-400">/10</span></div>
            <div className="text-xs text-gray-500 mt-1">Refined</div>
          </div>
        </div>
      </div>

      {/* Quality Breakdown */}
      <div className="bg-white rounded-lg border border-gray-200 p-4">
        <h2 className="text-lg font-semibold text-gray-800 mb-3">Quality Breakdown</h2>
        <div className="space-y-2">
          {qualityKeys.map(({ key, label }) => {
            const scores = prompt_quality_breakdown[key];
            return (
              <div key={key} className="flex items-center gap-2 text-sm">
                <span className="w-28 text-gray-600">{label}</span>
                <div className="flex-1 flex items-center gap-2">
                  <div className="w-8 text-right text-red-500 font-mono">{scores.original}</div>
                  <div className="flex-1 relative h-2 bg-gray-100 rounded-full overflow-hidden">
                    <div
                      className="absolute left-0 top-0 h-full bg-red-300 rounded-full"
                      style={{ width: `${scores.original * 10}%` }}
                    />
                  </div>
                  <div className="flex-1 relative h-2 bg-gray-100 rounded-full overflow-hidden">
                    <div
                      className="absolute left-0 top-0 h-full bg-green-400 rounded-full"
                      style={{ width: `${scores.refined * 10}%` }}
                    />
                  </div>
                  <div className="w-8 text-green-600 font-mono">{scores.refined}</div>
                </div>
              </div>
            );
          })}
          <div className="flex items-center gap-2 text-xs text-gray-400 mt-1">
            <span className="w-28" />
            <span className="flex-1 text-center">Original</span>
            <span className="flex-1 text-center">Refined</span>
            <span className="w-8" />
          </div>
        </div>
      </div>

      {/* Missing Elements */}
      {missing_elements.length > 0 && (
        <div className="bg-white rounded-lg border border-gray-200 p-4">
          <h2 className="text-lg font-semibold text-gray-800 mb-3">What Was Missing</h2>
          <div className="space-y-2">
            {missing_elements.map((item, i) => (
              <div key={i} className="border border-gray-100 rounded p-3 bg-gray-50">
                <div className="flex items-center gap-2">
                  <span className={`text-xs px-1.5 py-0.5 rounded font-medium ${
                    item.impact === "high" ? "bg-red-100 text-red-700" :
                    item.impact === "medium" ? "bg-yellow-100 text-yellow-700" :
                    "bg-blue-100 text-blue-700"
                  }`}>
                    {item.impact}
                  </span>
                  <span className="font-medium text-sm text-gray-800">{item.element}</span>
                </div>
                <p className="text-xs text-gray-500 mt-1">{item.explanation}</p>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Improvements Made */}
      {improvements_made.length > 0 && (
        <div className="bg-white rounded-lg border border-gray-200 p-4">
          <h2 className="text-lg font-semibold text-gray-800 mb-3">Improvements Made</h2>
          <div className="space-y-3">
            {improvements_made.map((item, i) => (
              <div key={i} className="border border-gray-100 rounded p-3">
                <div className="text-xs font-medium text-purple-600 uppercase mb-1">{item.category}</div>
                <div className="grid grid-cols-2 gap-2 text-sm">
                  <div>
                    <span className="text-xs text-gray-400">Before</span>
                    <div className="bg-red-50 rounded p-2 mt-0.5 text-gray-700 font-mono text-xs">{item.before}</div>
                  </div>
                  <div>
                    <span className="text-xs text-gray-400">After</span>
                    <div className="bg-green-50 rounded p-2 mt-0.5 text-gray-700 font-mono text-xs">{item.after}</div>
                  </div>
                </div>
                <p className="text-xs text-gray-500 mt-1">{item.why}</p>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
