from __future__ import annotations

import time

from sqlalchemy import inspect, text
from sqlalchemy.orm import Session

from backend.database import SessionLocal, engine
from backend.models import User
from backend.security import hash_password

ADMIN_EMAIL = "123456"
ADMIN_PASSWORD = "1234567"


def ensure_schema() -> None:
    """Ensure database schema changes (such as new columns) are applied."""
    with engine.begin() as conn:
        inspector = inspect(conn)
        if "users" not in inspector.get_table_names():
            return

        columns = {column["name"] for column in inspector.get_columns("users")}
        if "is_admin" not in columns:
            conn.execute(text("ALTER TABLE users ADD COLUMN is_admin BOOLEAN NOT NULL DEFAULT FALSE"))


def ensure_admin_user() -> None:
    """Create or update the built-in admin account."""
    with SessionLocal() as session:
        admin = session.query(User).filter(User.email == ADMIN_EMAIL).first()
        if admin is None:
            admin = User(
                email=ADMIN_EMAIL,
                full_name="系统管理员",
                hashed_password=hash_password(ADMIN_PASSWORD),
                is_admin=True,
            )
            session.add(admin)
            session.commit()
            session.refresh(admin)
        else:
            updated = False
            if not admin.is_admin:
                admin.is_admin = True
                updated = True
            # Optionally reset password to default each startup
            admin.hashed_password = hash_password(ADMIN_PASSWORD)
            updated = True
            if updated:
                session.add(admin)
                session.commit()


APP_START_TIME = time.time()
