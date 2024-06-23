from pydantic import BaseModel, ConfigDict


class GroupDayCreate(BaseModel):
    group: int
    period_1: int | None = None
    period_2: int | None = None
    period_3: int | None = None
    period_4: int | None = None
    period_5: int | None = None


class GroupDay(GroupDayCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


__all__ = ('GroupDayCreate', 'GroupDay')
