__all__ = ('router',)

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from . import crud
from .dependencies import period_by_id
from .schemas import Period, PeriodCreate
from core.models import db_helper

router = APIRouter(tags=['Periods'])


@router.get('/', response_model=list[Period])
async def get_periods(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_periods(session=session)


@router.post('/', response_model=Period, status_code=status.HTTP_201_CREATED)
async def create_tperiod(period_in: PeriodCreate, session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.create_period(period_in=period_in, session=session)


@router.get('/{period_id}', response_model=Period)
async def get_period(period: Period = Depends(period_by_id)):
    return period
