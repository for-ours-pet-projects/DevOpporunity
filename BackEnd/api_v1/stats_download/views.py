from fastapi import APIRouter
from fastapi import APIRouter, HTTPException, status, Depends
from . import hhru_api
from . import crud
from .dependencies import temp_by_id
from core.models.db_helper import db_helper_obj
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import TempCreate

router = APIRouter()


@router.get("/")
async def main():
    return 'hello world'


@router.get("/download")
async def download(
    session: AsyncSession = Depends(db_helper_obj.scoped_session_dependency),
):
    await crud.delete_temp(session)
    temp_update = hhru_api.download()
    async for vacancy_in in temp_update:
        await crud.create_temp(session=session, vacancy_in=vacancy_in)
    return await crud.get_temps(session=session)


@router.get("/drop")
async def download(
    session: AsyncSession = Depends(db_helper_obj.scoped_session_dependency),
):
    await crud.delete_temp(session)


@router.get("/merge")
async def download(
    session: AsyncSession = Depends(db_helper_obj.scoped_session_dependency),
):
    await crud.merge(session=session)
    return await crud.get_vacancies(session=session)
