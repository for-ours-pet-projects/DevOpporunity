from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.db_helper import db_helper_obj
from . import crud
from .dependencies import vacancy_by_id

from .schemas import VacancyBase, Vacancy

router = APIRouter()


@router.get("/", response_model=list[Vacancy])
async def get_vacancies(
    session: AsyncSession = Depends(db_helper_obj.scoped_session_dependency),
):
    return await crud.get_vacancies(session=session)


@router.get("/{vacancy_id}/", response_model=Vacancy)
async def get_vacancy(
    vacancy: Vacancy = Depends(vacancy_by_id),
):
    return vacancy

