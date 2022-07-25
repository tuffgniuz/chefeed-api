from typing import Optional, Union
from beanie.odm.fields import PydanticObjectId
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, InvalidPasswordException
from fastapi_users.fastapi_users import FastAPIUsers
from fastapi_users_db_beanie import ObjectIDIDMixin

from app.auth.auth_backend import auth_backend
from app.db import get_user_db
from app.config.settings import SECRET_KEY
from app.schemas.users import User, UserCreate, UserUpdate


class UserManager(ObjectIDIDMixin, BaseUserManager[User, PydanticObjectId]):
    reset_password_token_secret = SECRET_KEY
    verification_token_secret = SECRET_KEY

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f'User {user.id} has registered')

    async def on_after_forgot_password(self, user: User, token: str, request: Optional[Request] = None):
        print(f'User {user.id} has forgot their password. Reset token: {token}')

    async def on_after_request_verify(self, user: User, token: str, request: Optional[Request] = None):
        print(f'Verification requested for user {user.id}.')

    async def validate_password(self, password: str, user: Union[UserCreate, UserUpdate]) -> None:
        if len(password) < 8:
            raise InvalidPasswordException(
                reason='Password should be atleast 8 characters')
        if user.email in password:
            raise InvalidPasswordException(
                reason='Password should not contain e-mail')


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)

fastapi_users = FastAPIUsers[User, PydanticObjectId](
    get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)
