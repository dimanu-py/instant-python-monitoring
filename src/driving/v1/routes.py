from fastapi import APIRouter

from src.driving.v1.for_registering_usage import register_usage_router as register_usage


router = APIRouter(prefix="/app/v1", tags=["v1"])

router.include_router(register_usage.router)
