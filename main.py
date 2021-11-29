from fastapi import FastAPI
from api.v1.router import api_router

app  = FastAPI()

app.include_router(api_router)
