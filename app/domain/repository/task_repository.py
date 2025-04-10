from abc import ABC, abstractmethod
from domain.entity.task_entity import TaskEntity
from typing import List, Optional

class TaskRepository(ABC):
    @abstractmethod
    async def create(task:TaskEntity) -> TaskEntity:
        pass

    @abstractmethod
    async def update(id:int, task:TaskEntity) -> TaskEntity:
        pass

    @abstractmethod
    async def find(id: int) -> TaskEntity:
        pass

    @abstractmethod
    async def delete(id):
        pass

    @abstractmethod
    async def updateSuccess(id, status_id:int):
        pass

    @abstractmethod
    async def getByStatus(status_id: int, order_by:str) -> List[TaskEntity]:
        pass

    @abstractmethod
    async def getByapa():
        pass
    