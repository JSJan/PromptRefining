export default function ModelSelector({
  provider,
  onProviderChange,
  style,
  onStyleChange,
}) {
  return (
    <div className="flex gap-3">
      <select
        value={provider}
        onChange={(e) => onProviderChange(e.target.value)}
        className="px-3 py-2 border border-gray-300 rounded-lg text-sm bg-white"
      >
        <option value="openai">OpenAI</option>
        <option value="anthropic">Anthropic</option>
      </select>

      <select
        value={style}
        onChange={(e) => onStyleChange(e.target.value)}
        className="px-3 py-2 border border-gray-300 rounded-lg text-sm bg-white"
      >
        <option value="concise">Concise</option>
        <option value="balanced">Balanced</option>
        <option value="detailed">Detailed</option>
        <option value="structured">Structured</option>
      </select>
    </div>
  );
}
