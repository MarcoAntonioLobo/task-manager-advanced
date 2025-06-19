from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.task import Task
from app.services.task import get_tasks
from app.db.session import get_async_session

router = APIRouter()

@router.get("/", response_model=List[Task])
async def read_tasks(db: AsyncSession = Depends(get_async_session)):
    tasks = await get_tasks(db)
    return tasks
