import logging
from datetime import datetime

from src.dto.base import GwinstekDriverConfig, TelemetryFieldsHint
from src.models.driver import Driver

logger = logging.getLogger(__name__)


class GwinstekDriverService:
    """Сервис общения с источником питания"""
    def __init__(self, driver: Driver[GwinstekDriverConfig]):
        """Инициализация логики

        Args:
            driver (GwinstekDriverDTO): драйвер
        """
        self.driver = driver

    async def enable_channel(self, channel: int, current: float, voltage: float) -> None:
        """Включить канал питания

        Args:
            channel (int): Номер канала
            current (float): Ток
            voltage (float): Напряжение
        """
        await self.driver.run_command(f"SOURCE:CURRENT {current}, CH{channel}")
        await self.driver.run_command(f"SOURCE:VOLTAGE {voltage}, CH{channel}")
        await self.driver.run_command(f"OUTPUT:STATE ON, CH{channel}")
        logging.info("Канал %s включен", channel)

    async def disable_channel(self, channel: int) -> None:
        """Выключить канал питания

        Args:
            channel (int): Номер канала
        """
        await self.driver.run_command(f"OUTPUT{channel}:ON")
        logging.info("Канал %s выключен", channel)

    async def get_telemetry(self) -> list[TelemetryFieldsHint]:
        """Получить измерения по всем каналам

        Returns:
            list[TelemetryFieldsHint]: Список объектов с параметрами измерений
        """
        return [
            {
                "channel": i,
                "measured_dt": datetime.now(),
                "voltage": float(await self.driver.run_command(f"MEASURE{i}:VOLTAGE?")),
                "current": float(await self.driver.run_command(f"MEASURE{i}:CURRENT?")),
            } for i in range(1, self.driver.params.channels+1)
        ]
