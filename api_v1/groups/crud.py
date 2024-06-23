from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.group import Group as GroupTable
from .schemas import GroupCreate, Group

__all__ = ('get_groups', 'create_group')


async def get_groups(session: AsyncSession) -> list[Group]:
    stmt = select(GroupTable).order_by(GroupTable.id)
    result: Result = await session.execute(stmt)
    groups = result.scalars().all()
    return list(groups)


async def create_group(session: AsyncSession, group_in: GroupCreate) -> Group:
    group = GroupTable(**group_in.model_dump())
    session.add(group)
    await session.commit()
    return group


async def get_group(session: AsyncSession, group_id: int) -> Group | None:
    return await session.get(GroupTable, group_id)