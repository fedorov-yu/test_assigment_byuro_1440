from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field

from src.config import FLOAT_PRECISION


def round_float(value: float) -> float:
    """Округлить число до 2 знаков после запятой"""
    return round(value, FLOAT_PRECISION)


class TurnOnRequest(BaseModel):
    """Модель данных запроса метод `POST /driver/turnOn`"""
    channel: Annotated[int, Field(description="Канал включения сигнала", ge=0, examples=[1,2,34])]
    current: Annotated[float, Field(description="Величина тока", ge=0, examples=[1.0, 5.0])]
    voltage: Annotated[float, Field(description="Величина напряжения", ge=0, examples=[5.0, 12.0, 1.50])]


class TurnOffRequest(BaseModel):
    """Модель данных запроса метод `POST /driver/turnOff`"""
    channel: Annotated[int, Field(description="Канал выключения сигнала", ge=0, examples=[1, 2, 34])]


class HealthCheckDriverInfo(BaseModel):
    """Объект измерения показателей драйвера"""
    channel: Annotated[int, Field(description="Номер канала измерения")]
    measured_dt: Annotated[datetime, Field(description="ДатаВремя измерения")]
    current: Annotated[float, Field(description="Измеренный ток")]
    voltage: Annotated[float, Field(description="Измеренное напряжение")]
