from typing import Optional
from fastapi_users.manager import BaseUserManager
from starlette.requests import Request
from app.schemas.user import UserCreate, UserDisplay


SECRET = 'xxxxxxx'


class UserManager(BaseUserManager[UserCreate, UserDisplay]):
    user_db_model = UserDisplay
    reset_password_token = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: UserDisplay, request: Optional[Request] = None):
        '''
        Function called when user registration endpoint is triggered
        '''
        print(f'user {user.id} has registered')

    async def on_after_forgot_password(self, user: UserDisplay, token: str, request: Optional[Request] = None):
        print(
            f'User {user.id} has forgotten their password. Reset tokent: {token}')

    async def on_after_request_verify(self, user: UserDisplay, token: str, request: Optional[Request] = None):
        print(
            f'verification requested for {user.id} verification token: {token}')
