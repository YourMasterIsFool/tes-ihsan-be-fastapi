from interface.database.models.task_status import TaskStatus
from interface.database.db import get_session, create_db_and_tables, get_session_seeder
from sqlmodel import select
import asyncio


async def seeder():
    await create_db_and_tables()
    data = [
        {"code": "on_going", "name": "On Going"},
        {"code": "completed", "name": "Completed"},
    ]

    async with get_session_seeder() as session:
        for i in data:
            findDataQuery = select(TaskStatus).where(TaskStatus.code == i["code"])
            result = await session.exec(findDataQuery)
            result = result.one_or_none()
            if result is None:
                newData = TaskStatus(
                    name=i["name"], code=i["code"]
                )  
                session.add(newData)

        await session.commit()
        await session.close()
        print('seesder success')
