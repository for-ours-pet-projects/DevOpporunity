from fastapi import FastAPI
from api_v1.stats_download.views import router as stats_download_router
from api_v1.analytics.views import router as analytics_router

app = FastAPI()
app.include_router(stats_download_router, tags=['download'], prefix='/download')
app.include_router(analytics_router, tags=['analytics'], prefix='/analytics')
