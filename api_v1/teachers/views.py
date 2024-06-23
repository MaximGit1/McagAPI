__all__ = ('router',)

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from . import crud
from .dependencies import teacher_by_id
from .schemas import Teacher, TeacherCreate
from core.models import db_helper

router = APIRouter(tags=['Teachers'])


@router.get('/', response_model=list[Teacher])
async def get_teaches(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_teaches(session=session)


@router.post('/', response_model=Teacher, status_code=status.HTTP_201_CREATED)
async def create_teacher(teacher_in: TeacherCreate, session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.create_teacher(teacher_in=teacher_in, session=session)

@router.get('/{teacher_id}', response_model=Teacher)
async def get_product(teacher: Teacher = Depends(teacher_by_id)):
    return teacher
