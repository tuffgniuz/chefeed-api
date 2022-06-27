import redis.asyncio
from fastapi_users.authentication import AuthenticationBackend, BearerTransport, RedisStrategy

from app.config import settings

# SECRET_KEY = settings.SECRET_KEY

redis = redis.asyncio.from_url(settings.REDIS_URL, decode_responses=True)

bearer_transport = BearerTransport(tokenUrl='auth/login')


def get_redis_strategy() -> RedisStrategy:
    return RedisStrategy(redis, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name='redis',
    transport=bearer_transport,
    get_strategy=get_redis_strategy
)
