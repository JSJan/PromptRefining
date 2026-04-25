export default function RefinedOutput({ refinement }) {
  return (
    <div className="bg-white rounded-lg border border-gray-200 p-4">
      <div className="flex justify-between items-center mb-3">
        <h2 className="text-lg font-semibold text-gray-800">Refined Prompt</h2>
        <span className="text-xs bg-green-100 text-green-700 px-2 py-1 rounded">
          {refinement.refinement_style} · {refinement.model_used}
        </span>
      </div>
      <div className="bg-gray-50 rounded p-3 font-mono text-sm whitespace-pre-wrap border border-gray-100">
        {refinement.refined_prompt}
      </div>
      <button
        onClick={() => navigator.clipboard.writeText(refinement.refined_prompt)}
        className="mt-2 text-sm text-blue-600 hover:text-blue-800"
      >
        Copy to clipboard
      </button>
    </div>
  );
}
