import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || "",
});

export async function analyzePrompt(prompt, models = null) {
  const { data } = await api.post("/api/analyze", { prompt, models });
  return data;
}

export async function refinePrompt(
  prompt,
  provider = "openai",
  model = null,
  refinementStyle = "balanced"
) {
  const { data } = await api.post("/api/refine", {
    prompt,
    provider,
    model,
    refinement_style: refinementStyle,
  });
  return data;
}

export async function getModels() {
  const { data } = await api.get("/api/models");
  return data;
}
