from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
# from typing import TYPE_CHECKING
from .base import Base

# if TYPE_CHECKING:
#     from .teacher import Teacher


class Period(Base):
    __tablename__ = 'periods'

    lesson: Mapped[int] = mapped_column(ForeignKey("lessons.id"))
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teachers.id"))
    second_teacher_id: Mapped[int | None] = mapped_column(ForeignKey("teachers.id"), nullable=True)
    classroom: Mapped[int]

    # teacher: Mapped["Teacher"] = relationship(back_populates="period")
