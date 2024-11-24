from typing import Annotated

from fastapi import APIRouter, Depends

from ..dependecies.driver import get_driver_service
from ..dto.base import TelemetryFieldsHint
from ..schemas import driver as driver_schemas
from ..schemas.base import BaseStatusResponse
from ..services.driver import GwinstekDriverService

driver_router = APIRouter(prefix="/driver", tags=["driver"])


@driver_router.post("/turnOn", summary="Включить питание", response_model=BaseStatusResponse)
async def turn_on(
    data: driver_schemas.TurnOnRequest,
    service: Annotated[GwinstekDriverService, Depends(get_driver_service)]) -> dict[str, str]:
    """Метод включения питания"""
    await service.enable_channel(data.channel, current=data.current, voltage=data.voltage)
    return {"status": "success"}


@driver_router.post("/turnOff", summary="Выключить питание", response_model=BaseStatusResponse)
async def turn_off(
    data: driver_schemas.TurnOffRequest,
    service: Annotated[GwinstekDriverService, Depends(get_driver_service)]) -> dict[str, str]:
    """Метод выключения питания"""
    await service.disable_channel(data.channel)
    return {"status": "success"}


@driver_router.get(
        "/healthCheck",
        summary="Проверка состояния всех каналов",
        response_model=list[driver_schemas.HealthCheckDriverInfo],
        )
async def get_driver_state(
    service: Annotated[GwinstekDriverService, Depends(get_driver_service)]) -> list[TelemetryFieldsHint]:
    """Метод выключения питания"""
    return await service.get_telemetry()
