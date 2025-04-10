import domain.entity
import domain.entity.task_entity
from domain.repository.task_repository import TaskRepository
from domain.entity.task_entity import TaskEntity
from typing import List, Optional
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from sqlalchemy.orm import selectinload

from interface.database.models.task import Task
from datetime import datetime
from domain.entity import task_entity

class TaskRepositoryImpl(TaskRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
    async def find(self, id: str)->Optional[TaskEntity]:
        result = await self.session.get(Task, int(id))
        if result is None: 
            return None
        task  = result
        return TaskEntity(
            id= task.id,
            name= task.name,
            task_status_id= task.task_status_id,
            user_id= task.user_id,
            created_at=task.created_at,
            deleted_at=task.deleted_at
        )

    async def get(self) -> List[TaskEntity]:
        statement = select(Task).where(Task.deleted_at == None)
        result = await self.session.exec(statement)
        tasks = result
        return [
            TaskEntity(
                id=task.id,
                name=task.name,
                task_status_id=task.task_status_id,
                user_id=task.user_id,
                created_at=task.created_at
            )
            for task in tasks
        ]

    async def getByStatus(self, status_id: int, order_by: str) -> List[TaskEntity]:
        print(status_id, 'status id')
        sorting = Task.created_at.asc()
        if order_by == 'desc':
            sorting = Task.created_at.desc()
        statement = select(Task).options(selectinload(Task.task_status)).where(Task.deleted_at == None, Task.task_status_id == status_id).order_by(sorting)
        
        result = await self.session.exec(statement)
        
        return result.all()

    async def create(self, task:TaskEntity)->TaskEntity:
        model =  Task(
            name=task.name,
            task_status_id = task.task_status_id,
            user_id =  task.user_id,
            created_at= datetime.now()
        )
        self.session.add(model)
        await self.session.commit()
        await self.session.refresh(model)

        return TaskEntity(
            name =  model.name,
            task_status_id = model.task_status_id,
            user_id = model.user_id,
            created_at = model.created_at
        )

    async def update(self, id, task:TaskEntity):
        model =  select(Task).where(Task.id == int(id)).options(selectinload(Task.task_status))
        result =  await self.session.exec(model)
        modelUpdate = result.one()
        modelUpdate.name = task.name
        self.session.add(modelUpdate)
        await self.session.commit()
        await self.session.refresh(modelUpdate)

        return modelUpdate

    # soft delete
    async def delete(self, id: str):
        model =  select(Task).where(Task.id == int(id))
        result =  await self.session.exec(model)
        modelUpdate = result.one()
        modelUpdate.deleted_at =  datetime.now()
        self.session.add(modelUpdate)
        await self.session.commit()
        await self.session.refresh(modelUpdate)

        return modelUpdate

    async def updateSuccess(self, id, update_status:int):
        model =  select(Task).where(Task.id == int(id)).options(selectinload(Task.task_status))
        result =  await self.session.exec(model)
        modelUpdate = result.one()
        modelUpdate.task_status_id = update_status
        self.session.add(modelUpdate)
        await self.session.commit()
        await self.session.refresh(modelUpdate)

        return modelUpdate

    async def getByapa():
        pass