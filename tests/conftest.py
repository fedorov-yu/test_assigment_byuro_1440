
from typing import Any
import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient

from src.config import driver_config
from src.dto.base import GwinstekDriverConfig
from src.main import telemetry_driver_app
from src.models.driver import DriverGwinstek
from src.services.driver import GwinstekDriverService

channels_data = [
    {
        "channel": 1,
        "current": 1.0,
        "voltage": 3.3,
        },
    {
        "channel": 3,
        "current": 1.6,
        "voltage": 3.9,
        },
    {
        "channel": 2,
        "current": 0.2,
        "voltage": 3.3,
        },
    {
        "channel": 4,
        "current": 12,
        "voltage": 5,
        },
    ]

class MockDriver:
    def __init__(self, data: dict[str, int | float] | None = None) -> None:
        self.data = data

    async def mock_return_command(self, command: str, *args: Any) ->  int | float | str:
        """Имитация ответа от драйвера"""
        if "MEASURE" in command:
            param = command.split(":")[-1][:-1].lower()  # "voltage" | "current"
            return self.data.get(param)
        if "SOURCE" in command:
            return command.split(":")[-1].split(" ")[0] + "?"  # "VOLTAGE?" | "CURRENT?"
        return "OK\n"

    async def mock_run_command(self, command: str) -> str | float:
        """Мок для запуска команд на драйвере

        Args:
            command (str): команда

        Returns:
            str | float: имитация ответа драйвера
        """
        if "MEASURE" in command:
            return 1.0
        return "cool!"


@pytest.fixture()
def mock_driver(monkeypatch: pytest.MonkeyPatch):
    """Мок подключения к драйверу"""
    monkeypatch.setattr(DriverGwinstek, "run_command", MockDriver().mock_run_command)
    monkeypatch.setattr(DriverGwinstek, "connect", lambda: ...)
    monkeypatch.setattr(GwinstekDriverService, "log_telemetry", lambda: ...)

@pytest.fixture
async def async_client():
    """Мок клиент для запросов

    Yields:
        AsyncClient: Мок клиент
    """
    async with AsyncClient(app=telemetry_driver_app.app) as test_client:
        yield test_client

@pytest.fixture
def client():
    """Мок клиент для запросов"""
    return TestClient(telemetry_driver_app.app)


@pytest.fixture(params=channels_data)
def mock_command_data(monkeypatch: pytest.MonkeyPatch, request: pytest.FixtureRequest):
    """Фикстура для проверки сгеерированной команды

    Args:
        monkeypatch (pytest.MonkeyPatch): моккер
        request (pytest.FixtureRequest): обхект параметризации
    """
    monkeypatch.setattr(DriverGwinstek, "run_command", MockDriver(request.param).mock_return_command)
    return request.param


@pytest.fixture
def driver_service():
    """Фикстура сервиса для тестов"""
    return GwinstekDriverService(DriverGwinstek(GwinstekDriverConfig(**driver_config)))
