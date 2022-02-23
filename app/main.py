from fastapi import FastAPI
from fastapi.param_functions import Depends

from app.schemas.user import UserDisplay


from .api.auth.user import auth_backend, current_active_user, fastapi_users
# from .config import settings

app = FastAPI()

# TODO: add docstrings


# @app.on_event('startup')
# async def startup_db_client():
#     app.mongo_client = AsyncIOMotorClient(settings.DB_URL)
#     app.mongodb = app.mongo_client.chefeed_db


# @app.on_event('shutdown')
# async def shutdown_db_client():
#     app.mongo_client.close()


app.include_router(fastapi_users.get_auth_router(
    auth_backend), prefix='/auth/jwt', tags=['auth'])
app.include_router(fastapi_users.get_register_router(),
                   prefix='/auth', tags=['auth'])
app.include_router(fastapi_users.get_reset_password_router(),
                   prefix='/auth', tags=['auth'])
app.include_router(fastapi_users.get_verify_router(),
                   prefix='/auth', tags=['auth'])
app.include_router(fastapi_users.get_users_router(),
                   prefix='/users', tags=['users'])


@app.get('/authenticated-rout')
async def authenticated_route(user: UserDisplay = Depends(current_active_user)):
    return {'message': f'hello {user.email}'}
# app.include_router(UserRouter)
