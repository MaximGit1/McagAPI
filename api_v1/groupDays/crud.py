from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.groupDay import GroupDay as GroupDayTable
from .schemas import GroupDay, GroupDayCreate

## others
from ..groups.crud import get_group
from ..periods.crud import get_period
from ..teachers.crud import get_teacher
from ..lessons.crud import get_lesson

async def get_groupDays(session: AsyncSession) -> list[GroupDay]:
    stmt = select(GroupDayTable).order_by(GroupDayTable.id)
    result: Result = await session.execute(stmt)
    groupDays = result.scalars().all()
    return list(groupDays)


async def create_groupDay(session: AsyncSession, groupDay_in: GroupDayCreate) -> GroupDay:
    groupDay = GroupDayTable(**groupDay_in.model_dump())
    session.add(groupDay)
    await session.commit()
    return groupDay


async def get_groupDay(session: AsyncSession, groupDay_id: int) -> GroupDay | None:
    return await session.get(GroupDayTable, groupDay_id)

async def get_groupDays_read(session: AsyncSession):
    group_days_num = await get_groupDays(session=session)
    groups_title = []
    periods = []
    for group in group_days_num:
        groups_title.append((await get_group(session=session, group_id=group.group)).title)
        periods_current = [group.period_1, group.period_2, group.period_3, group.period_4, group.period_5]
        per_group = []
        for per_ in periods_current:
            per_info, per_num = [], ['period_1', 'period_2', 'period_3', 'period_4', 'period_5']
            per = await get_period(session=session, period_id=per_)
            if per is None:
                per_info.append(None)
                continue
            activities = {}
            if per is None:
                periods.append(None)
            activities['lesson'] = (await get_lesson(session=session, lesson_id=per.lesson)).title
            activities['teacher'] = (await get_teacher(session=session, teacher_id=per.teacher_id)).fio
            if per.second_teacher_id:
                activities['second_teacher_id'] = (await get_teacher(session=session, teacher_id=per.second_teacher_id)).fio
            else:
                activities['second_teacher_id'] = None
            activities['classroom'] = per.classroom
            per_info.append(activities)
            per_group.append(dict(zip(per_num, per_info)))
        periods.append(per_group)
    print(periods)
    return None
