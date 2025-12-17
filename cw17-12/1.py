import select
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey, create_engine, delete
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)


class Task(Base):
    __tablename__ = "tasks"
    task: Mapped[str] = mapped_column(String(255))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="belong_task")


class TaskCategory(Base):
    __tablename__ = "tasks_categories"
    task_id: Mapped["Task"] = relationship(back_populates="id")
    category_id: Mapped["Category"] = relationship(back_populates="id")


class User(Base):
    __tablename__ = "users"
    name: Mapped[str] = mapped_column(String(255))
    belong_tasks: Mapped[List["Task"]] = relationship(back_populates="user")


class Category(Base):
    __tablename__ = "categories"
    name: Mapped[str] = mapped_column(String(255))