__all__ = ('router',)

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from . import crud
from .dependencies import groupDay_by_id
from .schemas import GroupDay, GroupDayCreate
from core.models import db_helper

router = APIRouter(tags=['Groups day'])


@router.get('/', response_model=list[GroupDay])
async def getgroupDays(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_groupDays(session=session)


@router.post('/', response_model=GroupDay, status_code=status.HTTP_201_CREATED)
async def create_groupDay(groupDay_in: GroupDayCreate, session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.create_groupDay(groupDay_in=groupDay_in, session=session)

@router.get('/read')
async def getgroupDays_read(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_groupDays_read(session=session)


@router.get('/{groupDay_id}', response_model=GroupDay)
async def get_groupDay(groupDay: GroupDay = Depends(groupDay_by_id)):
    return groupDay


