import motor.motor_asyncio
from fastapi_users.db import BeanieUserDatabase

from app.models.user import User
from app.config.settings import MONGO_DB_URL

client = motor.motor_asyncio.AsyncIOMotorClient(
    MONGO_DB_URL,
    uuidRepresentation='standard'
)
db = client['chefeed-db']


async def get_user_db():
    yield BeanieUserDatabase(User)
