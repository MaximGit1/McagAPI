from pydantic import BaseModel, ConfigDict
from typing import Annotated
from annotated_types import MaxLen, MinLen


class GroupCreate(BaseModel):
    title: Annotated[str, MaxLen(15), MinLen(6)]


class Group(GroupCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


__all__ = ('GroupCreate', 'Group')
