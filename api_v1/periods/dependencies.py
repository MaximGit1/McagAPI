from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Period
from . import crud


async def period_by_id(period_id: Annotated[int, Path],
                        session: AsyncSession = Depends(db_helper.session_dependency)) -> Period:
    period = await crud.get_period(session=session, period_id=period_id)
    if period:
        return period
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Period {period_id} not found')
