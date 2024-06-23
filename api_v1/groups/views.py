__all__ = ('router',)

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from . import crud
from .dependencies import group_by_id
from .schemas import Group, GroupCreate
from core.models import db_helper

router = APIRouter(tags=['Groups'])


@router.get('/', response_model=list[Group])
async def get_groups(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_groups(session=session)


@router.post('/', response_model=Group, status_code=status.HTTP_201_CREATED)
async def create_group(group_in: GroupCreate, session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.create_group(group_in=group_in, session=session)


@router.get('/{group_id}', response_model=Group)
async def get_group(group: Group = Depends(group_by_id)):
    return group