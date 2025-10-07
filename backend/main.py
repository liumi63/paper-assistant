"""
FastAPI application entrypoint for the Paper Assistant backend.

Run locally with:
    uvicorn backend.main:app --reload
"""
from __future__ import annotations

from fastapi import FastAPI

from backend import bootstrap, models  # noqa: F401  # ensure models are registered
from backend.config import get_settings
from backend.database import Base, engine
from backend.routers import admin, auth

settings = get_settings()

app = FastAPI(title=settings.app_name)


@app.get("/health", tags=["system"])
async def health_check():
    """Simple readiness probe to confirm the API is running."""
    return {"status": "ok", "app": settings.app_name}


# Ensure tables exist for the configured models
Base.metadata.create_all(bind=engine)
bootstrap.ensure_schema()
bootstrap.ensure_admin_user()

# Register routers
app.include_router(auth.router)
app.include_router(admin.router)
