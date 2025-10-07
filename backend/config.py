"""
Basic configuration helpers for the FastAPI backend.

Loads environment variables (via python-dotenv when available) and exposes
centralised settings such as the database URL.
"""
from __future__ import annotations

import os
from functools import lru_cache

from dotenv import load_dotenv

# Load variables from .env at project root (if present).
load_dotenv()


class Settings:
    """Runtime configuration for the backend service."""

    def __init__(self) -> None:
        default_db = "postgresql+psycopg2://postgres:postgres@localhost:5432/paper_assistant"
        self.database_url = os.getenv("DATABASE_URL", default_db)
        self.app_name = os.getenv("APP_NAME", "Paper Assistant API")
        self.debug = os.getenv("DEBUG", "false").lower() == "true"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return a cached Settings instance so values are loaded once per process."""
    return Settings()
