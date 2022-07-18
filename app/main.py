from beanie import init_beanie
from fastapi import FastAPI

from app import db
from app.api.auth.login_manager import auth_backend, fastapi_users
from app.models.user import User, UserCreate, UserRead, UserUpdate

app = FastAPI()

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth',
    tags=['auth']
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['auth'],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix='/users',
    tags=['users']
)


@app.on_event('startup')
async def on_startup():
    await init_beanie(
        database=db.db,
        document_models=[
            User,
        ]
    )
