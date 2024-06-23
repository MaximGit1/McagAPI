from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Teacher
from . import crud


async def teacher_by_id(teacher_id: Annotated[int, Path],
                        session: AsyncSession = Depends(db_helper.session_dependency)) -> Teacher:
    teacher = await crud.get_teacher(session=session, teacher_id=teacher_id)
    if teacher:
        return teacher
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Product {teacher_id} not found')
