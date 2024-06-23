from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.period import Period as PeriodTable
from .schemas import Period, PeriodCreate

__all__ = ('get_periods', 'create_period')


async def get_periods(session: AsyncSession) -> list[Period]:
    stmt = select(PeriodTable).order_by(PeriodTable.id)
    result: Result = await session.execute(stmt)
    periods = result.scalars().all()
    return list(periods)


async def create_period(session: AsyncSession, period_in: PeriodCreate) -> Period:
    period = PeriodTable(**period_in.model_dump())
    session.add(period)
    await session.commit()
    return period


async def get_period(session: AsyncSession, period_id: int) -> Period | None:
    return await session.get(PeriodTable, period_id)
