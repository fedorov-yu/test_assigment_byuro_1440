import asyncio

from fastapi import FastAPI

from src.dto.base import GwinstekDriverConfig

from .app.base import TelemetryDriverApp
from .app.logger import colored_handler, init_logging
from .config import CUSTOM_LOGGERS, LOG_LEVEL, driver_config
from .models.driver import DriverGwinstek
from .routers import main_router
from .services.driver import GwinstekDriverService

init_logging(LOG_LEVEL, colored_handler, CUSTOM_LOGGERS)

async def lifespan(app: FastAPI):
    """Lifespan приложения"""
    service = GwinstekDriverService(DriverGwinstek(GwinstekDriverConfig(**driver_config)))
    asyncio.create_task(service.log_telemetry())
    yield
    service.driver.disconnect()


telemetry_driver_app = TelemetryDriverApp(
    app_type=FastAPI,
    main_router=main_router,
    lifespan=lifespan,
)
