from datetime import datetime

from sqlalchemy import select, update
from sqlalchemy.engine import Result
from core.models import Temp_vacancies, db_helper, Vacancy, City
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


async def merge(
    session: AsyncSession,
) -> None:
    temp_vacancies = await session.execute(select(Temp_vacancies))
    temp_vacancies = temp_vacancies.scalars().all()

    for temp in temp_vacancies:
        # Проверка, существует ли вакансия в основной таблице
        existing_vacancy = await session.execute(
            select(Vacancy).where(Vacancy.link == temp.link)
        )
        existing_vacancy = existing_vacancy.scalar()

        if existing_vacancy:
            # Обновление существующей вакансии
            await session.execute(
                update(Vacancy)
                .where(Vacancy.link == temp.link)
                .values(
                    name=temp.name,
                    description=temp.description,
                    salary_range_min=temp.salary_range_min,
                    salary_range_max=temp.salary_range_max,
                    date_disappearance=datetime.utcnow(),  # Обновляем время изменения
                    vacancy_id=temp.vacancy_id,
                )
            )
        else:
            # Добавление новой вакансии
            # Проверка, существует ли город
            city = await session.execute(select(City).where(City.city == temp.city))
            city = city.scalar()

            if not city:
                # Добавление нового города
                city = City(city=temp.city)
                session.add(city)
                await session.flush()  # Получение ID города

            # Добавление новой вакансии
            new_vacancy = Vacancy(
                name=temp.name,
                description=temp.description,
                link=temp.link,
                salary_range_min=temp.salary_range_min,
                salary_range_max=temp.salary_range_max,
                city_id=city.id,  # Использование ID города
                date_appearance=datetime.utcnow(),
                vacancy_id=temp.vacancy_id,
            )
            session.add(new_vacancy)

    # Сохранение изменений
    await session.commit()


async def get_vacancies(session: AsyncSession):
    stmt = select(Vacancy).order_by(Vacancy.id)
    result: Result = await session.execute(stmt)
    temps = result.scalars().all()
    return list(temps)
