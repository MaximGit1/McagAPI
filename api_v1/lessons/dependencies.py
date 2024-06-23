from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Lesson
from . import crud


async def lesson_by_id(lesson_id: Annotated[int, Path],
                        session: AsyncSession = Depends(db_helper.session_dependency)) -> Lesson:
    lesson = await crud.get_lesson(session=session, lesson_id=lesson_id)
    if lesson:
        return lesson
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Lesson {lesson_id} not found')
