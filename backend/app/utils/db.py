from app.db.session import SessionLocal
from typing import Optional, Callable, Any, Sequence
from fastapi import params
from .errors import CREDENTIALS_INVALID


def get_db():
    try:
        db = SessionLocal(user_id=None)
        yield db
    finally:
        db.close()



