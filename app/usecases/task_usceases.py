from domain.repository.task_repository import TaskRepository
from delivery.http.dto.task_dto import CreateTaskDto, UpdateTaskDto
from fastapi import HTTPException
from domain.entity.task_entity import TaskEntity
from utils.logging.custom_logging import logger
from typing import List
from usecases.task_status_usecase import TaskStatusUsecase
from interface.database.repository.task_status_repository_impl import TaskStatusRepositoryImpl
from interface.database.db import AsyncSession
from interface.database.db import get_session

class TaskUsecase:
    def __init__(self, repo: TaskRepository, session: AsyncSession):
        self.session = session
        self.repo = repo
    async def create(self, schema: CreateTaskDto) -> TaskEntity:

        taskStatusUsecase = TaskStatusUsecase(TaskStatusRepositoryImpl(self.session))
        findStatus = await taskStatusUsecase.getOngoingStatus()
        task_schema = TaskEntity(
            name=schema.name,
            task_status_id=findStatus.id
        )
        try:
            result = await self.repo.create(task_schema)
        except Exception as e:
            logger.error(f'error when create task {str(e)}')
            raise HTTPException(status_code=500, detail=f"Error creating task: {str(e)}")
        return result

    async def find(self, id:str) -> List[TaskEntity]:
        result = await self.repo.find(id)
        if result is None:
            raise HTTPException(404, detail=f"task id tidak ada dalam record")
        return result

    async def get(self) -> List[TaskEntity]:
        result = await self.repo.get()
        return result

    async def getOngoingTasks(self) -> List[TaskEntity]:

        taskStatusUsecase = TaskStatusUsecase(TaskStatusRepositoryImpl(self.session))
        findStatus = await taskStatusUsecase.getOngoingStatus()
        result = await self.repo.getByStatus(findStatus.id, 'desc')
        return result

    async def getCompletedTask(self) -> List[TaskEntity]:
        taskStatusUsecase = TaskStatusUsecase(TaskStatusRepositoryImpl(self.session))
        findStatus = await taskStatusUsecase.getCompletedStatus()
        result = await self.repo.getByStatus(findStatus.id, 'asc')
        return result

    async def update(self, id:int, schema: UpdateTaskDto):

        find = await self.find(id)
        try:
            taskEntity = TaskEntity(
               name= schema.name 
            )
            result = await self.repo.update(find.id, taskEntity)
        except Exception as e:
            logger.error(f'error when update task {str(e)}')
            raise HTTPException(status_code=500, detail=f"Error updating task")
        return result 

    async def delete(self, id:int,):
        find = await self.find(id);
        try:
            result = await self.repo.delete(id)
        except Exception as e:
            logger.error(f'error when delete task {str(e)}')
            raise HTTPException(status_code=500, detail=f"Error delete task: {str(e)}")
        return result 

    async def updateSuccess(self, id:int):
        find = await self.find(id);
        taskStatusUsecase = TaskStatusUsecase(TaskStatusRepositoryImpl(self.session))
        findStatus = await taskStatusUsecase.getCompletedStatus()
        try:
            result = await self.repo.updateSuccess(id, findStatus.id)
        except Exception as e:
            logger.error(f'error when update  task to succes {str(e)}')
            raise HTTPException(status_code=500, detail=f"Error task to success: {str(e)}")
        return result 
