import asyncio
import logging
from datetime import date, datetime

import aiofiles

from src.config import LOG_DELAY, LOG_PATH
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

    async def log_telemetry(self) -> None:
        """Залогировать параметры телеметрии"""
        while True:
            log_datas = await self.get_telemetry()
            async with aiofiles.open(LOG_PATH / f"log_{date.today()}.txt", "wb") as log_file:
                msg = "\n".join([self.__pretty_log(log) for log in log_datas])
                await log_file.write(msg)
            await asyncio.sleep(LOG_DELAY)

    @staticmethod
    def __pretty_log(data: TelemetryFieldsHint) -> str:
        """Причесать лог к строке

        Args:
            data (TelemetryFieldsHint): объект измерений

        Returns:
            str: строка для лога
        """
        return (
            f"{data['measured_dt']}:: CHANNEL:{data['channel']}::"
            f"CURRENT:{data['current']}:: VOLTAGE:{data['voltage']}"
        )
