from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.teacher import Teacher as TeacherTable
from .schemas import TeacherCreate, Teacher

__all__ = ('get_teaches',)


async def get_teaches(session: AsyncSession) -> list[Teacher]:
    stmt = select(TeacherTable).order_by(TeacherTable.id)
    result: Result = await session.execute(stmt)
    teacher = result.scalars().all()
    return list(teacher)


async def create_teacher(session: AsyncSession, teacher_in: TeacherCreate) -> Teacher:
    teacher = TeacherTable(**teacher_in.model_dump())
    session.add(teacher)
    await session.commit()
    # await session.refresh(teacher)
    return teacher


async def get_teacher(session: AsyncSession, teacher_id: int) -> Teacher | None:
    return await session.get(TeacherTable, teacher_id)