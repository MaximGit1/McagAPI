__all__ = ('router',)

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from . import crud
from .dependencies import lesson_by_id
from .schemas import Lesson, LessonCreate
from core.models import db_helper

router = APIRouter(tags=['Lessons'])


@router.get('/', response_model=list[Lesson])
async def get_lessons(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_lessons(session=session)


@router.post('/', response_model=Lesson, status_code=status.HTTP_201_CREATED)
async def create_lesson(lesson_in: LessonCreate, session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.create_lesson(lesson_in=lesson_in, session=session)


@router.get('/{lesson_id}')
async def get_lesson(lesson: Lesson = Depends(lesson_by_id)):
    return lesson
