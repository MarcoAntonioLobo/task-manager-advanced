# app/api/endpoints/health.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/", summary="Check API health")
async def health_check():
    return {"status": "ok"}
