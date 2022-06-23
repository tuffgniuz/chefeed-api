import motor.motor_asyncio
from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values('.env')

DB_ROOT_USERNAME = config['MONGO_INITDB_ROOT_USERNAME']
DB_ROOT_PASSWORD = config['MONGO_INITDB_ROOT_PASSWORD']
DB_HOST = config['MONGO_HOST']
DB_PORT = config['MONGO_PORT']

DB_URL = f'mongodb://{DB_ROOT_USERNAME}:{DB_ROOT_PASSWORD}@{DB_HOST}:{DB_PORT}'

# connect to mongodb client (for connect to Fastapi-users)
client = motor.motor_asyncio.AsyncIOMotorClient(DB_URL)
db = client["chefeed_db"]

# connect to mongodb client (with Pymongo)
pymongo_client = MongoClient(DB_URL)
py_db = pymongo_client["chefeed_db"]


user_collection = py_db['users']


# database -> chefeed_db
# database = client.chefeed_db

# collections
# user_collection = database.get_collection('users')
# recipe_collection = database.get_collection('recipes')
