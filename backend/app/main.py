import glob
from importlib import import_module
from os import path

from app import config
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


# if config.DEV_MODE:
#    import debugpy
#    debugpy.listen(("0.0.0.0", 5555))
#    debugpy.wait_for_client()

# "FMG Recycling",
app = FastAPI(
    title=config.PROJECT_NAME,
    description="",
    version="v1",
    openapi_url="/docs/openapi.json",
)


# CORS
origins = []

# Set all CORS enabled origins
if config.BACKEND_CORS_ORIGINS:
    origins_raw = config.BACKEND_CORS_ORIGINS.split(",")
    for origin in origins_raw:
        use_origin = origin.strip()
        origins.append(use_origin)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


files = glob.glob("app/routes/*.py")

files.sort()
for f in files:
    route = path.basename(f[:-3])
    if not route.startswith("__"):
        app.include_router(
            import_module("app.routes." + route).router,
            prefix="/" + route,
            tags=[route],
        )
