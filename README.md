# PromptRefiner

A prompt optimization tool that analyzes, refines, and estimates costs for LLM prompts. Supports both OpenAI and Anthropic models.

## What It Does

- **Token Analysis** — Counts tokens for your prompt across different models (GPT-4o, GPT-3.5-turbo, Claude 3.5 Sonnet, Claude 3 Haiku)
- **Cost Estimation** — Calculates input/output costs based on current model pricing
- **Prompt Refinement** — Uses LLM-powered analysis to rewrite your prompt for clarity, specificity, and efficiency
- **Side-by-Side Comparison** — View original vs. refined prompt with token count and cost differences
- **Multi-Provider Support** — Switch between OpenAI and Anthropic as the refinement engine

## Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python 3.11+ · FastAPI · Uvicorn |
| **Frontend** | React 18 · Vite · TailwindCSS |
| **Tokenization** | tiktoken (OpenAI) · anthropic-tokenizer |
| **LLM Providers** | OpenAI API · Anthropic API |
| **Testing** | pytest (backend) · Vitest (frontend) |

## Project Structure

```
PromptRefining/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI application entry point
│   │   ├── api/
│   │   │   └── routes/
│   │   │       ├── analyze.py   # Token counting & cost estimation
│   │   │       └── refine.py    # Prompt refinement endpoint
│   │   ├── core/
│   │   │   ├── config.py        # Settings & environment variables
│   │   │   └── pricing.py       # Model pricing data
│   │   ├── services/
│   │   │   ├── tokenizer.py     # Token counting service
│   │   │   ├── cost.py          # Cost calculation service
│   │   │   └── refiner.py       # LLM-based prompt refinement
│   │   └── models/
│   │       ├── request.py       # Pydantic request models
│   │       └── response.py      # Pydantic response models
│   ├── tests/
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── components/
│   │   │   ├── PromptInput.jsx
│   │   │   ├── AnalysisPanel.jsx
│   │   │   ├── RefinedOutput.jsx
│   │   │   ├── CostComparison.jsx
│   │   │   └── ModelSelector.jsx
│   │   ├── services/
│   │   │   └── api.js
│   │   └── utils/
│   │       └── formatters.js
│   ├── package.json
│   └── vite.config.js
├── README.md
├── CONTRIBUTING.md
├── ENHANCEMENTS.md
├── CHANGELOG.md
├── CurrentApp.md
├── localsetup.md
└── LICENSE
```

## Quick Start

```bash
# Clone
git clone https://github.com/your-username/PromptRefining.git
cd PromptRefining

# Backend
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # Add your API keys
uvicorn app.main:app --reload

# Frontend (new terminal)
cd frontend
npm install
npm run dev
```

Open [http://localhost:5173](http://localhost:5173) in your browser.

## API Keys Required

You need at least one of:
- **OpenAI API Key** — [Get one here](https://platform.openai.com/api-keys)
- **Anthropic API Key** — [Get one here](https://console.anthropic.com/settings/keys)

See [localsetup.md](localsetup.md) for detailed setup instructions.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/analyze` | Analyze token count and cost for a prompt |
| `POST` | `/api/refine` | Refine a prompt and return comparison |
| `GET` | `/api/models` | List supported models with pricing |
| `GET` | `/api/health` | Health check |

## Screenshots

_Coming soon — UI is under development._

## License

MIT — see [LICENSE](LICENSE) for details.
