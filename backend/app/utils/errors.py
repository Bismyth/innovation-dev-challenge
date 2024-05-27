from fastapi import HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED

INVALID_ACTION = HTTPException(
    status_code=401, detail="The action you are trying to perform is currently disabled.")
PERMISSION_DENIED = HTTPException(
    status_code=400, detail="Not enough permissions")
DISABLED_ACCOUNT = HTTPException(
    status_code=400, detail="Account is currently not active")
CREDENTIALS_INVALID = HTTPException(
    status_code=HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)
ITEM_NOT_FOUND = HTTPException(status_code=404, detail="Item not found")
USER_NOT_FOUND = HTTPException(status_code=404, detail="User does not exist")
USER_DUPLICATE = HTTPException(status_code=400, detail="User already exists")
# WRITE_ERROR = HTTPException(
# status_code=400, detail="Unable to write to object")


def HTTPError(msg, status_code=400):
  if isinstance(msg, Exception):
    msg = str(msg)
  return HTTPException(status_code=status_code, detail=msg)
