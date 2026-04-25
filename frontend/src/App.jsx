import { useState } from "react";
import PromptInput from "./components/PromptInput";
import AnalysisPanel from "./components/AnalysisPanel";
import RefinedOutput from "./components/RefinedOutput";
import CostComparison from "./components/CostComparison";
import ComparisonDetail from "./components/ComparisonDetail";
import CliTipsPanel from "./components/CliTipsPanel";
import ModelSelector from "./components/ModelSelector";
import { analyzePrompt, refinePrompt } from "./services/api";

export default function App() {
  const [prompt, setPrompt] = useState("");
  const [provider, setProvider] = useState("openai");
  const [style, setStyle] = useState("balanced");
  const [analysis, setAnalysis] = useState(null);
  const [refinement, setRefinement] = useState(null);
  const [loading, setLoading] = useState({ analyze: false, refine: false });
  const [error, setError] = useState(null);

  const handleAnalyze = async () => {
    if (!prompt.trim()) return;
    setLoading((prev) => ({ ...prev, analyze: true }));
    setError(null);
    try {
      const data = await analyzePrompt(prompt);
      setAnalysis(data);
    } catch (err) {
      setError(err.response?.data?.detail || "Analysis failed");
    } finally {
      setLoading((prev) => ({ ...prev, analyze: false }));
    }
  };

  const handleRefine = async () => {
    if (!prompt.trim()) return;
    setLoading((prev) => ({ ...prev, refine: true }));
    setError(null);
    try {
      const data = await refinePrompt(prompt, provider, null, style);
      setRefinement(data);
      setAnalysis(data.original_analysis);
    } catch (err) {
      setError(err.response?.data?.detail || "Refinement failed");
    } finally {
      setLoading((prev) => ({ ...prev, refine: false }));
    }
  };

  return (
    <div className="max-w-6xl mx-auto px-4 py-8">
      <header className="mb-8 text-center">
        <h1 className="text-3xl font-bold text-gray-900">PromptRefiner</h1>
        <p className="text-gray-500 mt-1">
          Analyze token usage, estimate costs, and refine your LLM prompts
        </p>
      </header>

      {error && (
        <div className="mb-4 p-3 bg-red-50 border border-red-200 text-red-700 rounded-lg">
          {error}
        </div>
      )}

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2 space-y-4">
          <PromptInput value={prompt} onChange={setPrompt} />

          <div className="flex flex-wrap gap-3">
            <ModelSelector
              provider={provider}
              onProviderChange={setProvider}
              style={style}
              onStyleChange={setStyle}
            />
            <button
              onClick={handleAnalyze}
              disabled={loading.analyze || !prompt.trim()}
              className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:opacity-50"
            >
              {loading.analyze ? "Analyzing..." : "Analyze"}
            </button>
            <button
              onClick={handleRefine}
              disabled={loading.refine || !prompt.trim()}
              className="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 disabled:opacity-50"
            >
              {loading.refine ? "Refining..." : "Refine"}
            </button>
          </div>

          {refinement && <RefinedOutput refinement={refinement} />}
          {refinement?.comparison && <ComparisonDetail comparison={refinement.comparison} />}
          {refinement?.comparison?.cli_tips && <CliTipsPanel cliTips={refinement.comparison.cli_tips} />}
        </div>

        <div className="space-y-4">
          {analysis && <AnalysisPanel analysis={analysis} />}
          {refinement && <CostComparison refinement={refinement} />}
        </div>
      </div>
    </div>
  );
}
