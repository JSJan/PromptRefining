from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.routes import analyze, refine

app = FastAPI(
    title="PromptRefiner API",
    description="Analyze, refine, and estimate costs for LLM prompts",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analyze.router, prefix="/api", tags=["Analysis"])
app.include_router(refine.router, prefix="/api", tags=["Refinement"])


@app.get("/api/health")
async def health_check():
    return {"status": "ok", "version": "0.1.0"}
