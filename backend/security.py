"""
Utility helpers for password hashing and verification.
"""
from __future__ import annotations

from passlib.context import CryptContext

# 使用 pbkdf2_sha256，避免 bcrypt 的 72 字节限制。
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")


def hash_password(plain_password: str) -> str:
    return pwd_context.hash(plain_password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
