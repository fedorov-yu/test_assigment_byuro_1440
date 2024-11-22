
from typing import Any

from fastapi import APIRouter, FastAPI


class TelemetryDriverApp:
    """Приложение"""

    def __init__(self, app_type: type[FastAPI], main_router: APIRouter, **kwargs: Any) -> None:
        """Конструктор приложения"""
        self._app = app_type(
            title="telemetry-driver-app",
            swagger_ui_parameters={
                "displayRequestDuration": True,
                "filter": True,
                "requestSnippetsEnabled": True,
            },
            **kwargs,
        )
        self._app.include_router(main_router)

    @property
    def app(self) -> FastAPI:
        """FastAPI приложение"""
        return self._app
