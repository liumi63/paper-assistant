"""
FastAPI application entrypoint for the Paper Assistant backend.

Run locally with:
    uvicorn backend.main:app --reload
"""
from __future__ import annotations

from fastapi import FastAPI

from backend.config import get_settings
from backend.routers import auth

settings = get_settings()

app = FastAPI(title=settings.app_name)


@app.get("/health", tags=["system"])
async def health_check():
    """Simple readiness probe to confirm the API is running."""
    return {"status": "ok", "app": settings.app_name}


# Register routers
app.include_router(auth.router)
