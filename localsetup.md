# Local Setup Guide

Complete instructions for setting up PromptRefiner on your machine.

## Prerequisites

| Tool | Version | Check |
|------|---------|-------|
| Python | 3.11+ | `python3 --version` |
| Node.js | 18+ | `node --version` |
| npm | 9+ | `npm --version` |
| Git | 2.x | `git --version` |

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/PromptRefining.git
cd PromptRefining
```

## 2. Backend Setup

### Create Virtual Environment

```bash
cd backend
python3 -m venv venv
```

### Activate Virtual Environment

```bash
# macOS / Linux
source venv/bin/activate

# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Windows (CMD)
.\venv\Scripts\activate.bat
```

### Install Dependencies

```bash
pip install -r requirements.txt

# For development (includes testing and linting tools)
pip install -r requirements-dev.txt
```

### Configure Environment Variables

```bash
cp .env.example .env
```

Edit `.env` with your API keys:

```env
# Required: At least one provider key
OPENAI_API_KEY=sk-your-openai-key-here
ANTHROPIC_API_KEY=sk-ant-your-anthropic-key-here

# Optional: Override defaults
DEFAULT_MODEL=gpt-4o
BACKEND_PORT=8000
CORS_ORIGINS=http://localhost:5173
```

### Getting API Keys

**OpenAI:**
1. Go to [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Click "Create new secret key"
3. Copy the key (it won't be shown again)

**Anthropic:**
1. Go to [console.anthropic.com/settings/keys](https://console.anthropic.com/settings/keys)
2. Click "Create Key"
3. Copy the key

### Run the Backend

```bash
uvicorn app.main:app --reload --port 8000
```

Verify it's running: [http://localhost:8000/api/health](http://localhost:8000/api/health)

API docs available at: [http://localhost:8000/docs](http://localhost:8000/docs)

## 3. Frontend Setup

Open a **new terminal** (keep the backend running).

```bash
cd frontend
npm install
```

### Configure Frontend Environment

```bash
cp .env.example .env
```

Edit `.env`:

```env
VITE_API_BASE_URL=http://localhost:8000
```

### Run the Frontend

```bash
npm run dev
```

Open [http://localhost:5173](http://localhost:5173) in your browser.

## 4. Verify Everything Works

1. Open [http://localhost:5173](http://localhost:5173)
2. Type a test prompt: `Explain quantum computing in simple terms`
3. Click "Analyze" — you should see token counts and costs
4. Click "Refine" — you should see a refined version of your prompt

## Running Tests

```bash
# Backend tests
cd backend
pytest -v

# Frontend tests
cd frontend
npm test
```

## Linting

```bash
# Backend
cd backend
ruff check .
black --check .

# Frontend
cd frontend
npm run lint
```

## Troubleshooting

### `ModuleNotFoundError: No module named 'tiktoken'`
```bash
pip install tiktoken
```

### `OPENAI_API_KEY not set` error
Make sure `.env` exists in the `backend/` directory and contains your key. Restart the server after editing.

### CORS errors in browser console
Ensure `CORS_ORIGINS` in `backend/.env` matches your frontend URL (`http://localhost:5173`).

### Port already in use
```bash
# Find and kill the process on port 8000
lsof -i :8000
kill -9 <PID>

# Or use a different port
uvicorn app.main:app --reload --port 8001
```

### Node.js version too old
```bash
# Using nvm
nvm install 18
nvm use 18
```
