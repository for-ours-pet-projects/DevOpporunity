from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from core.models import Vacancy


async def get_vacancies(session: AsyncSession) -> list[Vacancy]:
    stmt = select(Vacancy).options(joinedload(Vacancy.city)).order_by(Vacancy.id)
    result: Result = await session.execute(stmt)
    vacancies = result.scalars().all()
    return list(vacancies)


async def get_vacancy(session: AsyncSession, vacancy_id: int) -> Vacancy | None:
    stmt = (
        select(Vacancy)
        .filter(Vacancy.id == vacancy_id)
        .options(
            joinedload(Vacancy.city)
        )
    )
    result = await session.execute(stmt)
    vacancy = result.scalars().one_or_none()
    return vacancy
