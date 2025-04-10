from abc import ABC, abstractmethod
from domain.entity.task_status_entity import TaskStatusEntity
from typing import List, Optional


class TaskStatusRepory(ABC):
    @abstractmethod
    async def get() -> List[TaskStatusEntity]:
        pass

    # @abstractmethod
    # async def create(taskStatus: TaskStatusEntity) -> TaskStatusEntity:
    #     pass
    
    @abstractmethod
    async def findByName(name: str) -> TaskStatusEntity:
        pass
    
    @abstractmethod
    async def findByCode(code: str) -> TaskStatusEntity:
        pass

  
