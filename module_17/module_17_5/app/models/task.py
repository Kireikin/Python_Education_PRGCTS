# for homework in /models
from app.backend.db import Base
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models import user


class Task(Base):
    __tablename__ = "tasks"
    __table_args__ = {"extend_existing": True}  # многие ко многим?!

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    # Определяем отношение "многие к одному"
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True, index=True)  # Связь с User

    slug = Column(String, unique=True, index=True)
    user = relationship("User", back_populates="tasks")


if '__name__' == '__main__':
    from sqlalchemy.schema import CreateTable  # для проверки сборки
    print(CreateTable(Task.__table__))
    pass
