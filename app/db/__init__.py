import motor.motor_asyncio
from fastapi_users.db import BeanieUserDatabase

from app.config.settings import DB_URL
from app.schemas.users import User

client = motor.motor_asyncio.AsyncIOMotorClient(
    DB_URL, uuidRepresentation='standard'
)
db = client['chefeed-db']


async def get_user_db():
    yield BeanieUserDatabase(User)
