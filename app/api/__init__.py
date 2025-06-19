# app/api/__init__.py

from fastapi import APIRouter
from app.api import endpoints

router = APIRouter()

router.include_router(endpoints.router, prefix="/api/v1", tags=["API"])
