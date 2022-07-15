from typing import List, Optional
from beanie import PydanticObjectId
from beanie.odm.fields import Indexed, Link
from beanie.odm.views import View
from fastapi_users import schemas
from fastapi_users.db import BeanieBaseUser
from pydantic.fields import Field
from datetime import datetime

from app.schemas.review import Review
from app.schemas.recipe import Recipe


class User(BeanieBaseUser[PydanticObjectId]):
    avatar_url: Optional[str] = 'https://robohash.org/38'
    name: str = Field(...)
    biography: Optional[str] = Field(max_length=300)
    # recipes: Indexed(List[Link[Recipe]], unique=True) = []
    recipes: List[Link[Recipe]] = []
    followers: List[Link['User']] = []
    following: List[Link['User']] = []

    class Settings:
        name = 'users'
        validate_on_save = True


class UserRead(schemas.BaseUser[PydanticObjectId]):
    avatar_url: Optional[str]
    name: Optional[str]
    biography: Optional[str]
    recipes: List[Link[Recipe]] = []
    reviews: List[Link[Review]] = []
    followers: List[Link['User']]
    following: List[Link['User']]


class UserCreate(schemas.BaseUserCreate):
    name: str = Field(...)

    class Config:
        schema_extra = {
            'example': {
                'name': 'Tuff Gniuz',
                'email': 'tuffgniuz@wu.tang',
                'password': '123456',
            }
        }


class UserUpdate(schemas.BaseUserUpdate):
    recipes: Optional[List[Link[Recipe]]]
    avatar_url: Optional[str]
    name: Optional[str]
    biography: Optional[str] = Field(max_length=300)

    class Config:
        schema_extra = {
            'example': {
                'avatar_url': 'str',
                'name': 'str',
                'biography': 'str',
            }
        }

# class UserRecipes(View):
#     sumRecipes: int
#     sumFollowers: int
#     sumFollowing: int
#
#     class Settings:
#         source = User
#         pipeline = [
#             {
#
#             }
#         ]
