import asyncio
import logging
import socket
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from ..dto.base import DriverConfig, GwinstekDriverConfig

logger = logging.getLogger(__name__)
T_co = TypeVar("T_co", bound=DriverConfig, covariant=True)


class Driver(ABC, Generic[T_co]):
    """Абстрактная модель драйвера"""
    def __init__(self, params: T_co) -> None:
        """Конструктор класса

        Args:
            params (T_co): Исходные данные драйвера
        """
        self.params = params
        self._socket = None

    @property
    @abstractmethod
    async def connect(self) -> dict[str, str]:
        """Получить/установить соединение"""

    @abstractmethod
    def disconnect(self) -> None:
        """Отключить соединение"""

    @abstractmethod
    async def run_command(self, command: str) -> str:
        """Выполнить команду

        Args:
            command (str): текст команды

        Returns:
            str: ответ прибора
        """

class DriverGwinstek(Driver[GwinstekDriverConfig]):
    """Интерфейс для подключения к драйверу"""
    _READ_BUF_SIZE = 1024
    def __init__(self, params: GwinstekDriverConfig):
        """Инициализация логики

        Args:
            params (GwinstekDriverDTO): драйвер
        """
        super().__init__(params)

    @property
    async def connect(self):
        """Получить/установить соединение"""
        if not self._socket:
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            awaitable =  asyncio.to_thread(self._socket.connect, (self.params.host, self.params.port))
            task = asyncio.create_task(awaitable)
            await task
            logger.info("Connected to %s:%p", self.params.host, self.params.port)
        return self._socket

    def disconnect(self) -> None:
        if self._socket:
            self._socket.close()

    async def run_command(self, command: str) -> str:
        """Выполнить команду

        Args:
            command (str): текст команды

        Returns:
            str: ответ прибора
        """
        command += "\n"
        # пакуем блокирующий код в поток чтобы выполнить асинхронно
        writer = asyncio.create_task(asyncio.to_thread((await self.connect).sendall, command.encode()))
        reader = asyncio.create_task(asyncio.to_thread((await self.connect).recv, self._READ_BUF_SIZE))
        await writer
        response = await reader
        return response.decode()
