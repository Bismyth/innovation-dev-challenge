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


@router.get("/employees", response_model=List[models.Employee])
def get_employees(*, db: Session = Depends(utils.get_db)):
    employees = db.query(schemas.Employee).all()
    return employees
    


@router.get("/employee", response_model=models.Employee)
def get_employee(*, db: Session = Depends(utils.get_db), id: int):
    employee = db.query(schemas.Employee).filter(schemas.Employee.id == id).first()
    return employee


@router.post("/employee", response_model=models.Employee)
def create_employee(
    *,
    db: Session = Depends(utils.get_db),
    employee: models.Employee
):
    employee_data = employee.dict(exclude_unset=True)
    db_employee = schemas.Employee(**employee_data)
    db.add(db_employee)
    db.commit()
    
    return db_employee


@router.delete("/employee")
def delete_milestone_type_ref(
    *, db: Session = Depends(utils.get_db), id: int
):
    db.query(schemas.Employee).filter(schemas.Employee.id == id).delete()
    db.commit()

