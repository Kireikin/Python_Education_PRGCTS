# for homework in /models
from app.backend.db_lection import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"keep_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    # user - объект связи с таблицей с таблицей User, где back_populates='tasks':
    tasks = relationship("Task", back_populates="user")


from sqlalchemy.schema import CreateTable  # для проверки сборки
print(CreateTable(User.__table__))  # проверяем сборку
