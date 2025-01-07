# for homework in /routers
from fastapi import APIRouter, Depends, status, HTTPException
from slugify import slugify
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models import User, Task  # под вопросом? но в этом модуле подключаем обе таблицы в db!
from app.schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete

task = APIRouter(prefix="/task", tags=["task"])


@task.get("/")
async def all_task(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task).where(Task.id > 0)).all()
    if tasks is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There are no tasks')
    return tasks


@task.get("/task_id")
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task_for_id = db.scalar(select(Task).where(Task.id == task_id))
    if task_for_id is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task was not found')
    return task_for_id


@task.post("/create")  # не доделано см задание
async def create_task(db: Annotated[Session, Depends(get_db)], task_create_model: CreateTask, user_id: int):

    user = db.scalar(select(User).where(User.id == user_id))

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User was not found")

    db.execute(insert(Task).values(title=task_create_model.title,
                                   content=task_create_model.content,
                                   user_id=user.id,
                                   slug=slugify(task_create_model.title)))
    db.commit()

    return {'status_code': status.HTTP_201_CREATED,
            'transaction': 'Successful'}


@task.put("/update")
async def update_task(db: Annotated[Session, Depends(get_db)], task_id: int, updates_task: UpdateTask):
    user = db.scalar(select(Task).where(Task.id == task_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is task not found'
        )
    db.execute(update(Task).where(Task.id == task_id).values(title=updates_task.title,
                                                             content=updates_task.content,
                                                             priority=updates_task.priority))
    db.commit()
    return {
        'status code': status.HTTP_200_OK,
        'transaction': 'User update is succsseful'
    }


@task.delete("/delete")
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task was not found'
        )
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {
        'status code': status.HTTP_200_OK,
        'transaction': 'Task delete is succsseful'
    }
