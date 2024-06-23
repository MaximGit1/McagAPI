from pydantic import BaseModel, ConfigDict
from typing import Annotated
from annotated_types import MaxLen, MinLen


class PeriodCreate(BaseModel):
    lesson: int
    teacher_id: int
    second_teacher_id: int | None = None
    classroom: int


class Period(PeriodCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


__all__ = ('PeriodCreate', 'Period')
