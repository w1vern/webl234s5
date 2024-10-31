from fastapi import FastAPI, Depends, HTTPException

from site.api import router

app = FastAPI()
app.include_router(router)