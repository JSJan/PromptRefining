# Enhancements Roadmap

Planned features and improvements for PromptRefiner, organized by priority.

## Phase 1 — Core MVP (Current)

- [x] Token counting for OpenAI models (tiktoken)
- [x] Token counting for Anthropic models
- [x] Cost estimation based on current pricing
- [x] LLM-powered prompt refinement
- [x] Side-by-side original vs refined comparison
- [x] Model selector (OpenAI / Anthropic)
- [ ] Basic React UI with TailwindCSS
- [ ] FastAPI backend with `/analyze` and `/refine` endpoints

## Phase 2 — Enhanced Analysis

- [ ] **Prompt Scoring** — Rate prompts on clarity, specificity, structure, and token efficiency (1-10 scale)
- [ ] **Detailed Breakdown** — Show token count per section (system prompt, user prompt, examples)
- [ ] **Multiple Refinement Strategies** — Offer "Concise", "Detailed", "Structured", "Chain-of-Thought" refinement styles
- [ ] **Prompt Templates** — Pre-built templates for common tasks (code generation, summarization, classification, etc.)
- [ ] **History** — Save and revisit past prompt analyses (local storage or SQLite)

## Phase 3 — Multi-Provider Expansion

- [ ] **Google Gemini** — Add Gemini 1.5 Pro/Flash token counting and pricing
- [ ] **Mistral** — Add Mistral Large/Medium/Small support
- [ ] **Llama (via Groq/Together)** — Open-source model token counting
- [ ] **Custom Model Pricing** — Let users input custom per-token costs for self-hosted models
- [ ] **Provider Cost Comparison Table** — Show cost for the same prompt across all providers side-by-side

## Phase 4 — Advanced Features

- [ ] **Batch Analysis** — Upload multiple prompts (CSV/JSON) and get bulk analysis
- [ ] **Prompt Diff View** — Highlight exact changes between original and refined prompts (word-level diff)
- [ ] **Token Heatmap** — Visual representation of which words/phrases consume the most tokens
- [ ] **Prompt Version Control** — Track refinement iterations with version history
- [ ] **Export** — Export analysis results as PDF, Markdown, or JSON
- [ ] **API Rate Limiting Dashboard** — Show estimated API calls remaining based on usage

## Phase 5 — Collaboration & Deployment

- [ ] **User Authentication** — Sign in to save prompt history across devices
- [ ] **Team Workspaces** — Share refined prompts and templates within a team
- [ ] **Prompt Library** — Community-shared prompt collection with ratings
- [ ] **VS Code Extension** — Analyze and refine prompts directly in the editor
- [ ] **CLI Tool** — Command-line interface for CI/CD integration
- [ ] **Docker Deployment** — One-command deployment with Docker Compose
- [ ] **Cloud Hosting** — Deploy to Vercel (frontend) + Railway/Fly.io (backend)

## Phase 6 — Intelligence & Optimization

- [ ] **Auto-Optimization** — Iteratively refine prompts until token count is minimized while maintaining quality
- [ ] **A/B Testing** — Run the same query with original vs refined prompt and compare outputs
- [ ] **Prompt Security Scan** — Detect potential prompt injection vulnerabilities
- [ ] **Context Window Visualizer** — Show how much of the model's context window is used
- [ ] **Cost Forecasting** — Estimate monthly cost based on expected usage patterns
- [ ] **Fine-tuning Recommendations** — Suggest when fine-tuning would be more cost-effective than prompting

## Suggesting New Enhancements

Have an idea? Open a GitHub Issue with the `enhancement` label. See [CONTRIBUTING.md](CONTRIBUTING.md) for details.
