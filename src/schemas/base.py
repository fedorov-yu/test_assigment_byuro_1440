from pydantic import BaseModel


class BaseStatusResponse(BaseModel):
    """Модель базового ответа API"""
    status: str = "success"