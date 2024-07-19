from fastapi import APIRouter

from . import hhru_api

router = APIRouter(tags=['download'])

@router.get('/')
async def download():
    return await hhru_api.download()
