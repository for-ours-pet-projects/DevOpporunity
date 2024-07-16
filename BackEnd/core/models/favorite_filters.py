from sqlalchemy.orm import Mapped

from .base import Base
from .mixins import UserRelationMixin, CityRelationMixin


class Favorite_filter(UserRelationMixin, CityRelationMixin, Base):
    _user_back_populates = "favorite_filter"
    _city_back_populates = "favorite_filter"
    _city_id_nullable = True

    salary_range_min: Mapped[float]
    salary_range_max: Mapped[float]

