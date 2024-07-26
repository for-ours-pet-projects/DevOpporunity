import datetime

from sqlalchemy import text, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import CityRelationMixin

# бд с вакансиями, создавай миксины для частых соединений
class Vacancy(CityRelationMixin, Base):
    _city_back_populates = "vacancy"
    _city_id_nullable = True
    name: Mapped[str | None]
    description: Mapped[str | None]
    link: Mapped[str]
    salary_range_min: Mapped[float | None]
    salary_range_max: Mapped[float | None]
    vacancy_id: Mapped[str]
    # Даты появления и исчезновения, в исчезновении хранится дата последнего добавления в нашу бд
    date_appearance: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    date_disappearance: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=datetime.datetime.utcnow,
        nullable=True
    )
