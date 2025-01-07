# for homework in /routers
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models import User, Task  # под вопросом был в модуле 17_4 и ранее!
from app.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete

# from slugify import slugify


router_user = APIRouter(prefix="/user", tags=["user"])


@router_user.get("/")
async def all_user(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User).where(User.id > 0)).all()
    if users is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There are no users'
        )
    return users


@router_user.get("/user_id")
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )
    return user


@router_user.post("/create")
async def create_user(db: Annotated[Session, Depends(get_db)], add_user: CreateUser):
    db.execute(insert(User).values(username=add_user.username,  # параметры см в файле schemas.py?
                                   firstname=add_user.firstname,
                                   lastname=add_user.lastname,
                                   age=add_user.age))
    db.commit()
    return {
        'status code': status.HTTP_201_CREATED,
        'transaction': 'Succsseful'
    }


@router_user.put("/update")
async def update_user(db: Annotated[Session, Depends(get_db)], user_id: int, updates_user: UpdateUser):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is user not found'
        )
    db.execute(update(User).where(User.id == user_id).values(firstname=updates_user.firstname,
                                                             lastname=updates_user.lastname,
                                                             age=updates_user.age))
    db.commit()
    return {
        'status code': status.HTTP_200_OK,
        'transaction': 'User update is succsseful'
    }


@router_user.delete("/delete")
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    del_user = db.scalar(select(User).where(User.id == user_id))
    if del_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )
    db.execute(delete(User).where(User.id == user_id))
    db.execute(delete(Task).where(Task.user_id == user_id))
    db.commit()
    return {
        'status code': status.HTTP_200_OK,
        'transaction': 'User delete is succsseful'
    }


@router_user.get('/user_id/tasks')
async def tasks_by_user_id(
        db: Annotated[Session, Depends(get_db)],
        user_id: int
):
    tasks = list(db.scalars(select(Task).where(Task.user_id == user_id)))
    return tasks
