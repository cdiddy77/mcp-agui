from fastapi import APIRouter

from app.api.v1.example import router as example_router

router = APIRouter()

router.include_router(example_router, prefix="/example", tags=["example"])
