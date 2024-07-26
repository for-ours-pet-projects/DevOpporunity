import datetime

from pydantic import BaseModel, ConfigDict


class City(BaseModel):
    city: str | None
    id: int


class VacancyBase(BaseModel):
    name: str | None
    description: str | None
    link: str | None
    city: City | None
    salary_range_min: float | None
    salary_range_max: float | None
    vacancy_id: str
    date_appearance: datetime.datetime | None
    date_disappearance: datetime.datetime | None

    class Config:
        orm_mode = True


class Vacancy(VacancyBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
