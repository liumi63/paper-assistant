"""
Administrative monitoring endpoints.
"""
from __future__ import annotations

import time

from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.bootstrap import APP_START_TIME
from backend.config import get_settings
from backend.database import get_db
from backend.models import User

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/overview", summary="后端监控信息")
def overview(db: Session = Depends(get_db)):
    settings = get_settings()
    total_users = db.query(func.count(User.id)).scalar() or 0
    admin_users = db.query(func.count(User.id)).filter(User.is_admin.is_(True)).scalar() or 0
    uptime_seconds = int(time.time() - APP_START_TIME)

    return {
        "app": settings.app_name,
        "uptime_seconds": uptime_seconds,
        "uptime_human": _format_duration(uptime_seconds),
        "database_url": settings.database_url,
        "users": {
            "total": total_users,
            "admins": admin_users,
        },
        "checks": [
            {"title": "API 状态", "status": "ok", "detail": "FastAPI 服务运行正常"},
            {"title": "数据库连接", "status": "ok", "detail": "PostgreSQL 连接已建立"},
            {
                "title": "后台队列",
                "status": "pending",
                "detail": "队列功能尚未接入，未来用于文档解析与任务调度。",
            },
        ],
    }


def _format_duration(seconds: int) -> str:
    mins, sec = divmod(seconds, 60)
    hrs, mins = divmod(mins, 60)
    days, hrs = divmod(hrs, 24)
    parts = []
    if days:
        parts.append(f"{days} 天")
    if hrs:
        parts.append(f"{hrs} 小时")
    if mins:
        parts.append(f"{mins} 分钟")
    if sec or not parts:
        parts.append(f"{sec} 秒")
    return " ".join(parts)
