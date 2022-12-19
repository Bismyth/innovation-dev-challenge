import os
import secrets


# 60 minutes * 24 hours * 8 days = 8 days
SERVER_NAME = "localhost"
SERVER_HOST = "localhost"
# a string of origins separated by commas
PROJECT_NAME = "Dev Challenge"
DEV_MODE = True
BACKEND_CORS_ORIGINS = "http://localhost:3000"


SQLALCHEMY_DATABASE_URI = f"sqlite:///file:app.db?&uri=true"