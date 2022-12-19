import datetime
import enum
import json

import pytz
from sqlalchemy import Column, DateTime, Integer, String, inspect
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import object_session
from sqlalchemy.types import ARRAY, TypeDecorator


class CustomBase(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__

    def _asdict(self):
        # return lambda r: {c.name: str(getattr(r, c.name)) for c in r.__table__.columns}
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    @property
    def db(self):
        return object_session(self)



Base = declarative_base(cls=CustomBase)
