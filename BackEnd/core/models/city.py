from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .favorite_filters import Favorite_filter
    from .vacancy import Vacancy


class City(Base):
    city: Mapped[str] = mapped_column(unique=True)
    favorite_filter: Mapped[list["Favorite_filter"]] = relationship(back_populates='city')
    vacancy: Mapped[list["Vacancy"]] = relationship(back_populates='city')