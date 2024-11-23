import os
from typing import Final

LOG_LEVEL: Final[str] = os.getenv("LOG_LEVEL", "INFO").upper()

CUSTOM_LOGGERS: Final[list[str]] = [
    "uvicorn",
    "uvicorn.error",
    "uvicorn.access",
]

DriverConfig = {
    "host": "localhost",
    "port": 8010,
    "channels": 4,
}

FLOAT_PRECISION: Final[int] = 2
