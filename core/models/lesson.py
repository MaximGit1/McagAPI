from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from .base import Base


class Lesson(Base):
    __tablename__ = 'lessons'

    title: Mapped[str] = mapped_column(String(32), unique=True, index=True)

