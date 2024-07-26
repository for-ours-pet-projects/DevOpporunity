from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Vacancy
from core.models.db_helper import db_helper_obj
from . import crud


async def vacancy_by_id(
    vacancy_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper_obj.scoped_session_dependency),
) -> Vacancy:
    vacancy = await crud.get_vacancy(session=session, vacancy_id=vacancy_id)
    if vacancy is not None:
        return vacancy

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {vacancy_id} not found!",
    )
