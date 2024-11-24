from ..config import driver_config
from src.dto.base import GwinstekDriverConfig
from src.models.driver import DriverGwinstek
from src.services.driver import GwinstekDriverService


def get_driver_service() -> GwinstekDriverService:
    """Получить сервис для работы с драйвером"""
    return GwinstekDriverService(DriverGwinstek(driver_config(**driver_config)))
