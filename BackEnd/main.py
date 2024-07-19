from fastapi import FastAPI
from api_v1.stats_download.views import router as stats_download_router

app = FastAPI()
app.include_router(stats_download_router)