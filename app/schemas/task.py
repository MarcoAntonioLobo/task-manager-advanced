# app/schemas/task.py

from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional


class TaskBase(BaseModel):
    title: str = Field(..., example="Estudar FastAPI")
    description: Optional[str] = Field(None, example="Ler documentação oficial e testar exemplos")


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None


class TaskInDBBase(TaskBase):
    id: int
    is_completed: bool
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class Task(TaskInDBBase):
    pass
