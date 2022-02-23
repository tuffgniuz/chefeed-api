import app

from typing import Optional
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, FastAPIUsers
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy
)
from fastapi_users.db import MongoDBUserDatabase
from app.config.settings import get_user_db

from app.schemas.user import User, UserDisplay, UserCreate, UserUpdate

SECRET = 'xxxxxxx'


class UserManager(BaseUserManager[UserCreate, UserDisplay]):
    user_db_model = UserDisplay
    reset_password_token = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: UserDisplay, request: Optional[Request] = None):
        print(f'user {user.id} has registered')

    async def on_after_forgot_password(self, user: UserDisplay, token: str, request: Optional[Request] = None):
        print(
            f'User {user.name} has forgotten their password. Reset tokent: {token}')

    async def on_after_request_verify(self, user: UserDisplay, token: str, request: Optional[Request] = None):
        print(
            f'verification requested for {user.name}. verification token: {token}')


async def get_user_manager(user_db: MongoDBUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)


bearer_transport = BearerTransport(tokenUrl='auth/jwt/login')


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name='jwt',
    transport=bearer_transport,
    get_strategy=get_jwt_strategy
)
fastapi_users = FastAPIUsers(
    get_user_manager,
    [auth_backend],
    User,
    UserCreate,
    UserUpdate,
    UserDisplay
)


current_active_user = fastapi_users.current_user(active=True)
