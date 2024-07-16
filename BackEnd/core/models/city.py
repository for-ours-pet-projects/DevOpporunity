from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class City(Base):
    city: Mapped[str] = mapped_column(unique=True)
