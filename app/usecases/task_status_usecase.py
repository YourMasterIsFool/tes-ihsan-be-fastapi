from domain.repository.task_status_repository import TaskStatusRepory
from domain.entity import task_entity, task_status_entity
from fastapi.exceptions import HTTPException

class TaskStatusUsecase:
    def __init__(self, repo:TaskStatusRepory):
        self.repo =  repo
    async def findByName(self, name:str)->task_status_entity.TaskStatusEntity:
        result = await self.repo.findByName(name)
        if(result is None):
            raise HTTPException(404, 'Task Status Not Found')
        return result
    async def findByCode(self, code:str)->task_status_entity.TaskStatusEntity:
        result = await self.repo.findByCode(code)
        if(result is None):
            raise HTTPException(404, 'Task Status Not Found')
        return result
    async def getCompletedStatus(self)->task_status_entity.TaskStatusEntity:
        result = await self.findByCode('completed')
        return result
    async def getOngoingStatus(self) -> task_status_entity.TaskStatusEntity:
        result = await self.findByCode("on_going")
        return result
