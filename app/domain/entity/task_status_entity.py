from pydantic import BaseModel
from typing import Optional

class TaskStatusEntity(BaseModel):
    id: Optional[int]
    name: str
    code: str
    
    class Config:
        orm_mode = True
