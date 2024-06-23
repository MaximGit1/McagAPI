from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Group
from . import crud


async def group_by_id(group_id: Annotated[int, Path],
                        session: AsyncSession = Depends(db_helper.session_dependency)) -> Group:
    group = await crud.get_group(session=session, group_id=group_id)
    if group:
        return group
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Group {group_id} not found')
