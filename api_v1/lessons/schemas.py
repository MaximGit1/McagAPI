from pydantic import BaseModel, ConfigDict
from typing import Annotated
from annotated_types import MaxLen, MinLen


class LessonCreate(BaseModel):
    title: Annotated[str, MaxLen(32), MinLen(4)]


class Lesson(LessonCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


__all__ = ('LessonCreate', 'Lesson')
