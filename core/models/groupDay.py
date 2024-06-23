from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class GroupDay(Base):
    __tablename__ = 'groupDays'

    group: Mapped[int] = mapped_column(ForeignKey("groups.id"))
    period_1: Mapped[int | None] = mapped_column(ForeignKey("periods.id"), nullable=True)
    period_2: Mapped[int | None] = mapped_column(ForeignKey("periods.id"), nullable=True)
    period_3: Mapped[int | None] = mapped_column(ForeignKey("periods.id"), nullable=True)
    period_4: Mapped[int | None] = mapped_column(ForeignKey("periods.id"), nullable=True)
    period_5: Mapped[int | None] = mapped_column(ForeignKey("periods.id"), nullable=True)

