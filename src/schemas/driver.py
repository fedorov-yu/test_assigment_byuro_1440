from typing import Annotated
from pydantic import BaseModel, Field

from src.config import FLOAT_PRECISION


def round_float(value: float) -> float:
    """Округлить число до 2 знаков после запятой"""
    return round(value, FLOAT_PRECISION)


class TurnOnRequest(BaseModel):
    """Модель данных запроса метод `POST /driver/turnOn`"""
    channel: Annotated[int, Field(description="Канал включения сигнала", examples=[1,2,34])]
    current: Annotated[float, Field(description="Величина тока", examples=[1.0, 5.0])]
    voltage: Annotated[float, Field(description="Величина напряжения", examples=[5.0, 12.0, 1.50])]


class TurnOffRequest(BaseModel):
    """Модель данных запроса метод `POST /driver/turnOff`"""
    channel: Annotated[int, Field(description="Канал выключения сигнала", examples=[1, 2, 34])]
