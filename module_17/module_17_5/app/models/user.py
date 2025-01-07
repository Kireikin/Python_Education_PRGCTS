# for homework in /models
from app.backend.db import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.models import task


class User(Base):
    __tablename__ = "users"  # Имя таблицы в базе данных
    __table_args__ = {"keep_existing": True}  # один ко многим?!
    id = Column(Integer, primary_key=True, index=True)  # Уникальный идентификатор
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)  # Человекочитаемый URL
    tasks = relationship("Task", back_populates="user")
    # user - объект связи с таблицей с таблицей User, где back_populates='tasks':
    #  tasks = relationship("Task", back_populates="user")  # один user ко многим task


if '__name__' == '__main__':
    from sqlalchemy.schema import CreateTable  # для проверки сборки

    print(CreateTable(User.__table__))  # проверяем сборку
    pass
