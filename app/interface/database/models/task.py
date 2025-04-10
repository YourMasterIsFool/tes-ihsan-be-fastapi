from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from .user import User
from .task_status import TaskStatus
from datetime import datetime

class Task(SQLModel, table=True):
    __tablename__ = "task"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    task_status_id: Optional[int] = Field(default=None, foreign_key="task_status.id")
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    task_status: Optional[TaskStatus] = Relationship(back_populates="tasks")
    user: Optional[User] = Relationship(back_populates="tasks")
    deleted_at: Optional[datetime] =  Field(default=None)
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
