from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper_obj, Temp_vacancies

from . import crud


async def temp_by_id(
    temp_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper_obj.scoped_session_dependency),
) -> Temp_vacancies:
    temp = await crud.get_temp(session=session, temp_id=temp_id)
    if temp is not None:
        return temp

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {temp_id} not found!",
    )