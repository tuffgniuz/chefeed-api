from dotenv import dotenv_values

config = dotenv_values('.env')

SECRET_KEY = config['SECRET_KEY']

REDIS_HOST = config['REDIS_HOST']
REDIS_PORT = config['REDIS_PORT']

DB_ROOT_USERNAME = config['MONGO_INITDB_ROOT_USERNAME']
DB_ROOT_PASSWORD = config['MONGO_INITDB_ROOT_PASSWORD']
DB_HOST = config['MONGO_HOST']
DB_PORT = config['MONGO_PORT']

REDIS_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}'
DB_URL = f'mongodb://{DB_ROOT_USERNAME}:{DB_ROOT_PASSWORD}@{DB_HOST}:{DB_PORT}'
