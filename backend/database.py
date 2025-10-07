"""
Database helpers using SQLAlchemy.

This module exposes a SQLAlchemy engine and session factory pointed to the
PostgreSQL database defined in settings. Actual models/migrations can be added
in follow-up iterations.
"""
from __future__ import annotations

from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.config import get_settings

settings = get_settings()

# echo=True prints SQL for debugging; controlled via Settings.debug flag.
engine = create_engine(settings.database_url, echo=settings.debug, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)


@contextmanager
def session_scope():
    """
    Provide a transactional scope around a series of operations.

    Typical usage:
        with session_scope() as session:
            session.add(obj)
    """
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
