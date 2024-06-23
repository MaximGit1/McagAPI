from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, GroupDay
from . import crud


async def groupDay_by_id(groupDay_id: Annotated[int, Path],
                        session: AsyncSession = Depends(db_helper.session_dependency)) -> GroupDay:
    groupDay = await crud.get_groupDay(session=session, groupDay_id=groupDay_id)
    if groupDay:
        return groupDay
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'GroupDay {groupDay_id} not found')
