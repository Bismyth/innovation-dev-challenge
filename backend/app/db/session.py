from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app import config


class LoggableSession(Session):
    def __init__(self, *args, user_id=None, **kwargs):
        self.user_id = user_id
        super().__init__(*args, **kwargs)


engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(class_=LoggableSession, autocommit=False, autoflush=True, bind=engine)
