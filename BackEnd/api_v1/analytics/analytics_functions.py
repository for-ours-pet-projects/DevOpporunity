#from . import crud
import asyncio

import crud
import pandas as pd
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from core.models.db_helper import db_helper_obj


async def make_df():
    session = db_helper_obj.scoped_session_dependency()
    df = await crud.get_vacancies(session=session)

asyncio.run(make_df())
