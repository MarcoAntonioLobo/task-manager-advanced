# app/api/endpoints/__init__.py

from fastapi import APIRouter
from app.api.endpoints import health, task

router = APIRouter()

router.include_router(health.router, prefix="/health", tags=["Health Check"])
router.include_router(task.router, prefix="/tasks", tags=["Tasks"])
