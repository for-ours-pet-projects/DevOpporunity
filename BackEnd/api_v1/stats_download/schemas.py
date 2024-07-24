from pydantic import BaseModel, ConfigDict


class TempBase(BaseModel):
    name: str | None
    description: str | None
    link: str | None
    city: str | None
    salary_range_min: float | None
    salary_range_max: float | None
    vacancy_id: str


class TempCreate(TempBase):
    pass


class Temp_vacancies(TempBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
