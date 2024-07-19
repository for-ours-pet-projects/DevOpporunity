from sqlalchemy.orm import Mapped

from .base import Base
from .mixins import CityRelationMixin


class Vacancy(CityRelationMixin, Base):
    _city_back_populates = "favorite_filter"
    _city_id_nullable = True
    name: Mapped[str]
    description: Mapped[str]
    link: Mapped[str]
    salary_range_min: Mapped[float]
    salary_range_max: Mapped[float]

