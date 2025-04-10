from domain.repository.task_repository import TaskRepository
from interface.database.repository.task_repository_impl import TaskRepositoryImpl
from pydantic import BaseModel
from domain.entity.task_entity import TaskEntity
from fastapi.exceptions import HTTPException
from fastapi import APIRouter, Depends
from interface.database.db import AsyncSession, get_session
from delivery.http.dto.task_dto import CreateTaskDto,UpdateTaskDto
from usecases.task_usceases import TaskUsecase
from utils.response.success_response import SuccessResponse
from typing import List

# router
router =  APIRouter(
    prefix='/api/tasks'
)
@router.post('/create',
response_model=SuccessResponse[TaskEntity]             
)
async def create_task(schema: CreateTaskDto, session: AsyncSession = Depends(get_session)):
    repo =  TaskRepositoryImpl(session)
    taskUsecase =  TaskUsecase(repo, session=session)
    result = await taskUsecase.create(schema)
    return SuccessResponse(data=result)

@router.get('/list/on_going',
    response_model=SuccessResponse[List[TaskEntity]]
)
async def get_task_on_going(session: AsyncSession = Depends(get_session)):
    repo =  TaskRepositoryImpl(session)
    taskUsecase =  TaskUsecase(repo, session=session)
    result = await taskUsecase.getOngoingTasks()
    return SuccessResponse(data=result)

@router.get("/list/completed", response_model=SuccessResponse[List[TaskEntity]])
async def get_list_completed(session: AsyncSession = Depends(get_session)):
    repo = TaskRepositoryImpl(session)
    taskUsecase = TaskUsecase(repo, session=session)
    result = await taskUsecase.getCompletedTask()
    return SuccessResponse(data=result)

@router.get("/list", response_model=SuccessResponse[List[TaskEntity]])
async def get_list_task(session: AsyncSession = Depends(get_session)):
    repo = TaskRepositoryImpl(session)
    taskUsecase = TaskUsecase(repo, session=session)
    result = await taskUsecase.get()
    return SuccessResponse(data=result)


@router.get('/detail/{id}',
    response_model=SuccessResponse[TaskEntity]
)
async def get_detail(id:int, session: AsyncSession = Depends(get_session)):
    repo =  TaskRepositoryImpl(session)
    taskUsecase =  TaskUsecase(repo, session=session)
    result = await taskUsecase.find(id)
    return SuccessResponse(data=result)

@router.delete('/delete/{id}')
async def delete_task(id: str, session: AsyncSession = Depends(get_session)):
    repo =  TaskRepositoryImpl(session)
    taskUsecase =  TaskUsecase(repo, session=session)
    result = await taskUsecase.delete(id=id)
    return SuccessResponse(data=result)

@router.put('/update/{id}',
response_model=SuccessResponse[TaskEntity]
)
async def update_task(id: str,schema:UpdateTaskDto, session: AsyncSession = Depends(get_session)):
    repo =  TaskRepositoryImpl(session)
    taskUsecase =  TaskUsecase(repo, session=session)
    result = await taskUsecase.update(id=id, schema=schema)
    return SuccessResponse(data=result)


@router.put('/update-success/{id}',
response_model=SuccessResponse[TaskEntity]
)
async def update_success(id: str, session: AsyncSession = Depends(get_session)):
    repo =  TaskRepositoryImpl(session)
    taskUsecase =  TaskUsecase(repo, session=session)
    result = await taskUsecase.updateSuccess(id=id)
    return SuccessResponse(data=result)
