from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from dto.base import DriverDTO, GwinstekDriverDTO

T_co = TypeVar("T_co", bound=DriverDTO, covariant=True)


class Driver(ABC, Generic[T_co]):
    """Абстрактная модель драйвера"""
    def __init__(self, data: T_co) -> None:
        """Конструктор класса

        Args:
            data (T_co): Исходные данные драйвера
        """
        self._data = data

    @abstractmethod
    def turn_on(self) -> dict[str, str]:
        pass


    @abstractmethod
    def turn_off(self) -> dict[str, str]:
        pass


    @abstractmethod
    def health_check(self) -> list[T_co]:
        pass


class DriverGwinstek(Driver[GwinstekDriverDTO]):
    """"""
    def __init__(self, data: GwinstekDriverDTO):
        """"""
        super().__init__(data)

    def turn_on(self) -> dict[str, str]:
        return super().turn_on()

    def turn_off(self) -> dict[str, str]:
        return super().turn_off()

