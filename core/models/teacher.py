from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Teacher(Base):
    __tablename__ = 'teachers'

    fio: Mapped[str] = mapped_column(unique=True)
    #lessons: Mapped[List["Lesson"]] = relationship(back_populates="teacher")

