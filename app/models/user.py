from typing import Optional
from beanie import Link, PydanticObjectId
from fastapi_users import schemas
from fastapi_users.db import BeanieBaseUser

from app.models.recipe import Recipe


class User(BeanieBaseUser[PydanticObjectId]):
    avatar_url: Optional[str]
    name: Optional[str]
    biography: Optional[str]

    recipe_ids: list[Link[Recipe]] = []


class UserRead(schemas.BaseUser[PydanticObjectId]):
    pass
    # name: Optiona[]
    # biography: str
    # avatar_url: str
    # recipe_ids: list[Link[Recipe]]


class UserCreate(schemas.BaseUserCreate):
    pass

    class Config:
        schema_extra = {
            'example': {
                'email': 'tuffgniuz@wu.tang',
                'password': '12345678',
            }
        }


class UserUpdate(schemas.BaseUserUpdate):
    pass
