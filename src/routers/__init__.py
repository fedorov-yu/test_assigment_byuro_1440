from fastapi import APIRouter

from .driver import driver_router
from .service import service_router

main_router = APIRouter()
main_router.include_router(service_router)
main_router.include_router(driver_router)