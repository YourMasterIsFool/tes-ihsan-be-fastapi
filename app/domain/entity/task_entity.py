from pydantic import BaseModel
from typing import Optional
from domain.entity.task_status_entity import TaskStatusEntity
from datetime import datetime

class TaskEntity(BaseModel):
    id: Optional[int] = None
    name: str
    task_status_id: Optional[int] = None
    user_id: Optional[int] =  None
    created_at: Optional[datetime] =  None
    deleted_at:Optional[datetime] =  None
    task_status: Optional[TaskStatusEntity] =  None
    class Config:
        orm_mode = True
