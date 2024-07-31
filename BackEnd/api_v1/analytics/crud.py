import datetime

from sqlalchemy import select, func, case
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from core.models import Vacancy, City


async def get_vacancies(session: AsyncSession) -> list[Vacancy]:
    stmt = select(Vacancy).options(joinedload(Vacancy.city)).order_by(Vacancy.id)
    result: Result = await session.execute(stmt)
    vacancies = result.scalars().all()
    return list(vacancies)


async def get_vacancy(session: AsyncSession, vacancy_id: int) -> Vacancy | None:
    stmt = (
        select(Vacancy)
        .filter(Vacancy.id == vacancy_id)
        .options(joinedload(Vacancy.city))
    )
    result = await session.execute(stmt)
    vacancy = result.scalars().one_or_none()
    return vacancy


async def get_avg_by_day(session: AsyncSession, day: datetime.date, cities: list):
    stmt = select(
        func.avg((Vacancy.salary_range_min + Vacancy.salary_range_max) / 2).label(
            "avg"
        ),
        func.avg(Vacancy.salary_range_min).label("avg_min"),
        func.avg(Vacancy.salary_range_max).label("avg_max"),
    ).filter(
        case((cities != [], Vacancy.city_id.in_(cities)), else_=True),
        Vacancy.date_disappearance >= day,
        Vacancy.date_appearance <= day,
    )

    result = await session.execute(stmt)
    row = result.one()
    return {"avg": row.avg,
            "avg_min": row.avg_min,
            "avg_max": row.avg_max}
