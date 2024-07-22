from sqlalchemy.orm import Mapped

from .base import Base



class Temp_vacancies(Base):
    name: Mapped[str | None]
    description: Mapped[str | None]
    link: Mapped[str | None]
    city: Mapped[str | None]
    salary_range_min: Mapped[float | None]
    salary_range_max: Mapped[float | None]