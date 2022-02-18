import motor.motor_asyncio
from dotenv import dotenv_values

config = dotenv_values('.env')

MONGO_ROOT_USERNAME = config['MONGO_INITDB_ROOT_USERNAME']
MONGO_ROOT_PASSWORD = config['MONGO_INITDB_ROOT_PASSWORD']
MONGO_HOST = config['MONGO_HOST']
MONGO_PORT = config['MONGO_PORT']

MONGO_URL = f'mongodb://{MONGO_ROOT_USERNAME}:{MONGO_ROOT_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}'

# connect to mongodb client
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)

# database -> chefeed_db
database = client.chefeed_db

# collections
user_collection = database.get_collection('users')
recipe_collection = database.get_collection('recipes')
