from domain.repository.task_status_repository import TaskStatusRepory
from domain.entity.task_status_entity import TaskStatusEntity
from typing import List
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from interface.database.models.task_status import TaskStatus
from typing import Optional


class TaskStatusRepositoryImpl(TaskStatusRepory):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self) -> List[TaskStatusEntity]:
        statement = select(TaskStatusEntity)
        result = await self.session.exec(statement)
        tasks = result
        return [
            TaskStatusEntity(id=task.id, name=task.name, code=task.code)
            for task in tasks
        ]
    
    async def findByName(self, name:str)->Optional[TaskStatusEntity]:
        stmt = select(TaskStatus).where(TaskStatus.name == name)
        result = self.session.exec(stmt)
        return result
    

    async def findByCode(self, code:str)->Optional[TaskStatusEntity]:
        stmt = select(TaskStatus).where(TaskStatus.code == code)
        result = await self.session.exec(stmt)
        result = result.one_or_none()

        if result is None:
            return None
        return TaskStatusEntity(
            name= result.name,
            id= result.id,
            code=result.code
        )