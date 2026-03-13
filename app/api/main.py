from fastapi import FastAPI

from app.api.routers.analysis import router as analysis_router
from app.api.routers.health import router as health_router
from app.api.routers.locations import router as locations_router
from app.api.routers.reports import router as reports_router
from app.core.config import settings
from app.core.logger import configure_logging

configure_logging()
app = FastAPI(title=settings.app_name, version=settings.app_version)

app.include_router(health_router)
app.include_router(analysis_router)
app.include_router(reports_router)
app.include_router(locations_router)
