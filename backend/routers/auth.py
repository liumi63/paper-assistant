"""
Authentication-related API endpoints.

These are non-persistent placeholders that demonstrate how the FastAPI
application will accept registration and login requests. Replace with real
database logic once user models are defined.
"""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy.orm import Session
from typing import Optional

from backend.database import SessionLocal

router = APIRouter(prefix="/auth", tags=["auth"])


def get_db():
    """Provide a SQLAlchemy session for request handlers."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    full_name: Optional[str] = None


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


@router.post("/register", summary="注册新用户")
def register(payload: RegisterRequest, db: Session = Depends(get_db)):
    """
    接收注册请求的占位实现。

    TODO:
        * 添加密码哈希与验证
        * 检查邮箱唯一性并写入数据库
        * 返回认证令牌
    """
    # TODO: replace with database logic
    del db  # prevent unused parameter warning while the handler is a stub
    return {
        "message": "注册接口待实现，当前仅验证请求结构。",
        "email": payload.email,
        "full_name": payload.full_name,
    }


@router.post("/login", summary="用户登录")
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    """
    接收登录请求的占位实现。

    TODO:
        * 校验用户存在
        * 验证密码并返回 JWT / 会话
    """
    # TODO: replace with database logic
    del db
    if payload.password == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="密码不能为空")

    return {
        "message": "登录接口待实现，当前仅验证请求结构。",
        "email": payload.email,
    }
