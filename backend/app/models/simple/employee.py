from app import schemas
from .base import Base
from typing import List


class Employee(Base):
    id : int = None
    first_name : str = None
    last_name : str = None
    email : str = None
    role : str = None
    active : bool = None



