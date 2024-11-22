from typing import Annotated
from fastapi import APIRouter, Depends
from schemas import driver as driver_schemas
from schemas.base import BaseStatusResponse
from src.dependecies.driver import get_driver_service
from src.services.driver import GwinsekDriverService

driver_router = APIRouter(prefix="/driver", tags=["driver"])


@driver_router.post("/turnOn", summary="Включить питание", response_model=BaseStatusResponse)
async def turn_on(driver_data: driver_schemas.TurnOnRequest) -> dict[str, str]:
    """Метод включения питания"""
    return {"status": "success"}


@driver_router.post("/turnOff", summary="Выключить питание", response_model=BaseStatusResponse)
async def turn_off(driver_data: driver_schemas.TurnOffRequest) -> dict[str, str]:
    """Метод выключения питания"""
    return {"status": "success"}


@driver_router.get("/healthCheck", summary="Проверка состояния всех каналов")
async def get_driver_state(logic: Annotated[GwinsekDriverService,  Depends(get_driver_service)]) -> BaseStatusResponse:
    """Метод выключения питания"""
    return {"status": "success"}