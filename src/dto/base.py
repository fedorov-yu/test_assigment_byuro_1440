from dataclasses import dataclass
from datetime import datetime
from typing import TypedDict


class TelemetryFieldsHint(TypedDict):
    """"""
    channel: int
    measured_dt: datetime
    current: float
    voltage: float

@dataclass
class DriverConfig:
    """"""
    host: str
    port: int


@dataclass
class GwinstekDriverConfig(DriverConfig):
    """"""
    channels: int
