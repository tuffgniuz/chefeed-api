from typing import Optional
from beanie.odm.fields import PydanticObjectId
from fastapi import Depends, Request
from fastapi_users import BaseUserManager
from fastapi_users.fastapi_users import FastAPIUsers
from fastapi_users_db_beanie import ObjectIDIDMixin

from app.auth.auth_backend import auth_backend
from app.db import get_user_db
from app.config.settings import SECRET_KEY
from app.schemas.users import User


class UserManager(ObjectIDIDMixin, BaseUserManager[User, PydanticObjectId]):
    reset_password_token_secret = SECRET_KEY
    verification_token_secret = SECRET_KEY

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f'User {user.id} has registered')

    async def on_after_forgot_password(self, user: User, token: str, request: Optional[Request] = None):
        print(f'User {user.id} has forgot their password. Reset token: {token}')

    async def on_after_request_verify(self, user: User, token: str, request: Optional[Request] = None):
        print(f'Verification requested for user {user.id}.')


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)

fastapi_users = FastAPIUsers[User, PydanticObjectId](
    get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)
