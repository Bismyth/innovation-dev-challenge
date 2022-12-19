from sqlalchemy.orm import Session

# make sure all SQL Alchemy models are imported before initializing DB
# otherwise, SQL Alchemy might fail to initialize properly relationships
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28
# from app.db import base  # noqa
from app import config, models, schemas, utils

# from fastapi import HTTPException

# from app import config


def init_db(db: Session):
    pass


init_db(next(utils.get_db()))
