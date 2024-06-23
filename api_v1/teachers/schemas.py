from pydantic import BaseModel, ConfigDict
from typing import Annotated
from annotated_types import MaxLen, MinLen


class TeacherCreate(BaseModel):
    fio: Annotated[str, MaxLen(25), MinLen(5)]


class Teacher(TeacherCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


__slots__ = ('TeacherCreate', 'Teacher')
