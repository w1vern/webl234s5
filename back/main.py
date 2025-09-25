
from fastapi import FastAPI

from back.api import router
from back.rabbit import router as rabbit_router

app = FastAPI(docs_url="/api/docs", redoc_url="/api/redoc",
              openapi_url="/api/openapi.json")
app.include_router(router)
app.include_router(rabbit_router)
