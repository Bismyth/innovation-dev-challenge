from app import schemas
from .base import Base
from typing import List


class Product(Base):
  id: int = None
  name: str = None
  description: str = None
  price: int = None
  category: str = None
  taxable: bool = None
  active: bool = None
