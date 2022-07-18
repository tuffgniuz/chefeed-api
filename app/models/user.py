from typing import Optional
from beanie import Link, PydanticObjectId
from fastapi_users import schemas
from fastapi_users.db import BeanieBaseUser


class User(BeanieBaseUser[PydanticObjectId]):
    avatar_url: Optional[str] = None
    name: Optional[str] = None
    biography: Optional[str] = None


class UserRead(schemas.BaseUser[PydanticObjectId]):
    pass
    # avatar_url: Optional[str]
    # biography: Optional[str]


class UserCreate(schemas.BaseUserCreate):
    pass

    class Config:
        schema_extra = {
            'example': {
                'email': 'tuffgniuz@wu.tang',
                'password': '12345678'
            }
        }


class UserUpdate(schemas.BaseUserUpdate):
    pass
