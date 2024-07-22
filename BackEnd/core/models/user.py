from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .favorite_filters import Favorite_filter

class User(Base):
    email: Mapped[str] = mapped_column(unique=True)
    is_active: Mapped[bool]
    is_verified: Mapped[bool]
    is_superuser: Mapped[bool]
    hashed_password: Mapped[str]
    favorite_filter: Mapped[list["Favorite_filter"]] = relationship(back_populates="user")
