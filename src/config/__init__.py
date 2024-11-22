import os
from typing import Final

LOG_LEVEL: Final[str] = os.getenv("LOG_LEVEL", "INFO").upper()

CUSTOM_LOGGERS: Final[list[str]] = [
    "uvicorn",
    "uvicorn.error",
    "uvicorn.access",
]


FLOAT_PRECISION: Final[int] = 2