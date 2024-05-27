import datetime as dt
from os import error, rename, path
from urllib.parse import urlencode
from typing import List
import requests
from fastapi import APIRouter, Depends  # Body,
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app import config, models, utils, schemas

router = APIRouter()


@router.get("/products", response_model=List[models.Product])
def get_products(*, db: Session = Depends(utils.get_db)):
  products = db.query(schemas.Product).all()
  return products


@router.get("/product", response_model=models.Product)
def get_product(*, db: Session = Depends(utils.get_db), id: int):
  product = db.query(schemas.Product).filter(schemas.Product.id == id).first()
  if product is None:
    raise utils.errors.ITEM_NOT_FOUND
  return product


@router.post("/product", response_model=models.Product)
def create_product(
    *,
    db: Session = Depends(utils.get_db),
    product: models.Product
):
  product_data = product.dict(exclude_unset=True)
  db_product = schemas.Product(**product_data)
  db.add(db_product)
  db.commit()

  return db_product


@router.put("/product", response_model=models.Product)
def update_product(
    *,
    db: Session = Depends(utils.get_db),
    product: models.Product,
    id: int
):
  db_product = db.query(schemas.Product).filter(
      schemas.Product.id == id).first()

  if product is None:
    raise utils.errors.ITEM_NOT_FOUND

  product_data = product.dict(exclude_unset=True)
  for k in product_data:
    db_product[k] = product_data[k]

  db.commit()
  db.refresh(db_product)

  return db_product


@router.delete("/product")
def delete_milestone_type_ref(
    *, db: Session = Depends(utils.get_db), id: int
):
  db.query(schemas.Product).filter(schemas.Product.id == id).delete()
  db.commit()
