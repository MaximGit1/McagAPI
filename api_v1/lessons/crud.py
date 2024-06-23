from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.lesson import Lesson as LessonTable
from .schemas import Lesson, LessonCreate

__all__ = ('get_lessons', 'create_lesson')


async def get_lessons(session: AsyncSession) -> list[Lesson]:
    stmt = select(LessonTable).order_by(LessonTable.id)
    result: Result = await session.execute(stmt)
    lessons = result.scalars().all()
    return list(lessons)


async def create_lesson(session: AsyncSession, lesson_in: LessonCreate) -> Lesson:
    lesson = LessonTable(**lesson_in.model_dump())
    session.add(lesson)
    await session.commit()
    return lesson


async def get_lesson(session: AsyncSession, lesson_id: int) -> Lesson | None:
    return await session.get(LessonTable, lesson_id)
