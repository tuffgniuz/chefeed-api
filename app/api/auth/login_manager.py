from beanie import PydanticObjectId
import redis.asyncio

from fastapi_users.exceptions import InvalidPasswordException
from typing import Optional, Union
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, FastAPIUsers
from fastapi_users.db import ObjectIDIDMixin
from fastapi_users.authentication import AuthenticationBackend, BearerTransport, RedisStrategy

from app.config.settings import SECRET_KEY, REDIS_HOST, REDIS_PORT
from app.db import get_user_db
from app.models.user import User, UserCreate, UserUpdate


class UserManager(ObjectIDIDMixin, BaseUserManager[User, ObjectIDIDMixin]):
    reset_password_token_secret = SECRET_KEY
    verification_token_secret = SECRET_KEY

    async def on_after_register(self, user: User, request: Optional[Request] = None) -> None:
        print(f'{user.id} has been created')

    async def on_after_request_verify(self, user: UserUpdate, token: str, request: Optional[Request] = None) -> None:
        print(f'Verificationr equested for {user.id}')

    # async def validate_password(self, password: str, user: Union[UserCreate, UserUpdate]) -> None:
    #     if len(password) < 8:
    #         raise InvalidPasswordException(
    #             reason='Password should be at least 8 characters')
    #     if user.email in password:
    #         raise InvalidPasswordException(
    #             reason='Password should not contain e-mail'
    #         )


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)

redis = redis.asyncio.from_url(
    f'redis://{REDIS_HOST}:{REDIS_PORT}', decode_responses=True)

bearer_transport = BearerTransport(tokenUrl='auth/redis/login')


def get_redis_strategy() -> RedisStrategy:
    return RedisStrategy(redis, lifetime_seconds=None)


auth_backend = AuthenticationBackend(
    name='redis',
    transport=bearer_transport,
    get_strategy=get_redis_strategy,
)

fastapi_users = FastAPIUsers[User, PydanticObjectId](
    get_user_manager, [auth_backend]
)

current_active_user = fastapi_users.current_user(active=True)
