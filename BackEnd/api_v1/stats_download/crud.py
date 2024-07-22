from sqlalchemy import select
from sqlalchemy.engine import Result
from core.models import Temp_vacancies, db_helper
from sqlalchemy.ext.asyncio import AsyncSession
from . import hhru_api
from .schemas import TempCreate
from sqlalchemy import delete

async def get_temps(session: AsyncSession) -> list[Temp_vacancies]:
    stmt = select(Temp_vacancies).order_by(Temp_vacancies.id)
    result: Result = await session.execute(stmt)
    temps = result.scalars().all()
    return list(temps)


async def get_temp(session: AsyncSession, temp_id: int) -> Temp_vacancies | None:
    return await session.get(Temp_vacancies, temp_id)


async def create_temp(session: AsyncSession, vacancy_in: dict) -> Temp_vacancies:
    vacancy_in_pydantic = TempCreate(**vacancy_in)
    vacancy = Temp_vacancies(**vacancy_in_pydantic.model_dump())
    session.add(vacancy)
    await session.commit()
    # await session.refresh(product)
    return vacancy


async def delete_temp(
    session: AsyncSession,
) -> None:
    await session.execute(delete(Temp_vacancies))
    await session.commit()

