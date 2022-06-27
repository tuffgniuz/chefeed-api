from typing import List, Optional
from beanie import PydanticObjectId
from beanie.odm.fields import Link
from beanie.odm.views import View
from fastapi_users import schemas
from fastapi_users.db import BeanieBaseUser
from pydantic.fields import Field

from app.schemas.recipe import Recipe


class User(BeanieBaseUser[PydanticObjectId]):
    biography: Optional[str] = Field(max_length=300)
    recipes: List[Link[Recipe]] = []
    followers: List[Link['User']] = []
    following: List[Link['User']] = []


class UserRead(schemas.BaseUser[PydanticObjectId]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass

    class Config:
        schema_extra = {
            'example': {
                'email': 'tuffgniuz@dev.io',
                'password': '123456',
            }
        }


class UserUpdate(schemas.BaseUserUpdate):
    recipes: Optional[List[Link[Recipe]]]
    # pass


# class UserPublicView(View):
