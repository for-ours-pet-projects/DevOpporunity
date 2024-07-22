from sqlalchemy.orm import Mapped

from .base import Base



class Temp_vacancies(Base):
    name: Mapped[str]
    description: Mapped[str]
    link: Mapped[str]
    city: Mapped[str]
    salary_range_min: Mapped[float]
    salary_range_max: Mapped[float]