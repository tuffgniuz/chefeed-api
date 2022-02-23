# import motor.motor_asyncio
from fastapi_users.db import MongoDBUserDatabase
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import dotenv_values

from app.schemas.user import UserDisplay

config = dotenv_values('.env')

DB_ROOT_USERNAME = config['MONGO_INITDB_ROOT_USERNAME']
DB_ROOT_PASSWORD = config['MONGO_INITDB_ROOT_PASSWORD']
DB_HOST = config['MONGO_HOST']
DB_PORT = config['MONGO_PORT']

DB_URL = f'mongodb://{DB_ROOT_USERNAME}:{DB_ROOT_PASSWORD}@{DB_HOST}:{DB_PORT}'

# connect to mongodb client
client = AsyncIOMotorClient(DB_URL, uuidRepresentation='standard')

# database -> chefeed_db
db = client.chefeed_db

# collections
user_collection = db['users']
# recipe_collection = database.get_collection('recipes')


async def get_user_db():
    yield MongoDBUserDatabase(UserDisplay, user_collection)
