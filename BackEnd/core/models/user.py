from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
    email: Mapped[str] = mapped_column(unique=True)
    is_active: Mapped[bool]
    is_verified: Mapped[bool]
    is_superuser: Mapped[bool]
    hashed_password: Mapped[str]
