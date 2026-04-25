export default function CliTipsPanel({ cliTips }) {
  if (!cliTips) return null;

  const { claude_cli, copilot_cli, general_tips } = cliTips;

  return (
    <div className="space-y-4">
      {/* Claude CLI */}
      {claude_cli.length > 0 && (
        <div className="bg-white rounded-lg border border-gray-200 p-4">
          <h2 className="text-lg font-semibold text-gray-800 mb-1">Claude CLI Tips</h2>
          <p className="text-xs text-gray-400 mb-3">Commands and flags for the <code className="bg-gray-100 px-1 rounded">claude</code> CLI</p>
          <div className="space-y-2">
            {claude_cli.map((tip, i) => (
              <div key={i} className="border border-gray-100 rounded p-3 bg-gray-50">
                <code className="text-sm font-semibold text-orange-600">{tip.command}</code>
                <p className="text-xs text-gray-600 mt-1">{tip.description}</p>
                <div className="mt-1.5 bg-gray-900 text-green-400 rounded p-2 text-xs font-mono overflow-x-auto">
                  {tip.example}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Copilot CLI */}
      {copilot_cli.length > 0 && (
        <div className="bg-white rounded-lg border border-gray-200 p-4">
          <h2 className="text-lg font-semibold text-gray-800 mb-1">GitHub Copilot Tips</h2>
          <p className="text-xs text-gray-400 mb-3">Commands for <code className="bg-gray-100 px-1 rounded">gh copilot</code> and VS Code Copilot Chat</p>
          <div className="space-y-2">
            {copilot_cli.map((tip, i) => (
              <div key={i} className="border border-gray-100 rounded p-3 bg-gray-50">
                <code className="text-sm font-semibold text-blue-600">{tip.command}</code>
                <p className="text-xs text-gray-600 mt-1">{tip.description}</p>
                <div className="mt-1.5 bg-gray-900 text-green-400 rounded p-2 text-xs font-mono overflow-x-auto">
                  {tip.example}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* General Tips */}
      {general_tips.length > 0 && (
        <div className="bg-white rounded-lg border border-gray-200 p-4">
          <h2 className="text-lg font-semibold text-gray-800 mb-3">General Tips</h2>
          <ul className="space-y-1.5">
            {general_tips.map((tip, i) => (
              <li key={i} className="flex items-start gap-2 text-sm text-gray-600">
                <span className="text-green-500 mt-0.5">✓</span>
                <span>{tip}</span>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}
