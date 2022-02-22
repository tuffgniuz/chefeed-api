# import motor.motor_asyncio
from dotenv import dotenv_values

config = dotenv_values('.env')

DB_ROOT_USERNAME = config['MONGO_INITDB_ROOT_USERNAME']
DB_ROOT_PASSWORD = config['MONGO_INITDB_ROOT_PASSWORD']
DB_HOST = config['MONGO_HOST']
DB_PORT = config['MONGO_PORT']

DB_URL = f'mongodb://{DB_ROOT_USERNAME}:{DB_ROOT_PASSWORD}@{DB_HOST}:{DB_PORT}'

# connect to mongodb client
# client = motor.motor_asyncio.AsyncIOMotorClient(DB_URL)

# database -> chefeed_db
# database = client.chefeed_db

# collections
# user_collection = database.get_collection('users')
# recipe_collection = database.get_collection('recipes')
