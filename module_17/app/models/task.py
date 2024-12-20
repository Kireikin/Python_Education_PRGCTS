# for homework in /models
from app.backend.db_lection import Base
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Task(Base):
    __tablename__ = "tasks"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)  # целое число, внешний ключ на id из таблицы
    # 'users', не NULL, с индексом.
    slug = Column(String, unique=True, index=True)  # целое число, внешний ключ на id из таблицы 'users', не NULL,
    # с индексом.

    # user - объект связи с таблицей с таблицей User, где back_populates='tasks':
    user = relationship("User", back_populates="tasks")


from sqlalchemy.schema import CreateTable  # для проверки сборки
print(CreateTable(Task.__table__))
