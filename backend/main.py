from fastapi import FastAPI
from .api.server import router as server_router
from .config import Settings

settings = Settings()

app = FastAPI(
    title=settings.app_title,
    version=settings.app_version,
    description=settings.app_description,
)

app.include_router(server_router, prefix="/api")
