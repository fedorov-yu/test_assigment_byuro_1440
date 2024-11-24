import os
from pathlib import Path
from typing import Final

LOG_LEVEL: Final[str] = os.getenv("LOG_LEVEL", "INFO").upper()

LOG_PATH = Path.cwd() / "logs"
LOG_DELAY = 5
CUSTOM_LOGGERS: Final[list[str]] = [
    "uvicorn",
    "uvicorn.error",
    "uvicorn.access",
]

driver_config: dict[str, str | int] = {
    "host": "localhost",
    "port": 8010,
    "channels": 4,
}

FLOAT_PRECISION: Final[int] = 2
