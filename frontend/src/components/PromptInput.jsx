export default function PromptInput({ value, onChange }) {
  return (
    <div>
      <label
        htmlFor="prompt"
        className="block text-sm font-medium text-gray-700 mb-1"
      >
        Your Prompt
      </label>
      <textarea
        id="prompt"
        rows={8}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder="Paste your prompt here..."
        className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 resize-y font-mono text-sm"
      />
      <div className="text-xs text-gray-400 mt-1 text-right">
        {value.length} characters · ~{value.split(/\s+/).filter(Boolean).length}{" "}
        words
      </div>
    </div>
  );
}
