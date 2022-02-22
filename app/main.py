from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from .api.api_v1.endpoints.user import router as UserRouter
from .config import settings

app = FastAPI()

# TODO: add docstrings


@app.on_event('startup')
async def startup_db_client():
    app.mongo_client = AsyncIOMotorClient(settings.DB_URL)
    app.mongodb = app.mongo_client.chefeed_db


@app.on_event('shutdown')
async def shutdown_db_client():
    app.mongo_client.close()


app.include_router(UserRouter)
