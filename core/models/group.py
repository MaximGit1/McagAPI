from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Group(Base):
    __tablename__ = 'groups'

    title: Mapped[str] = mapped_column(String(15), unique=True)
