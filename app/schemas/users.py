from typing import List, Optional
from beanie import PydanticObjectId
from beanie.odm.fields import Link
from beanie.odm.views import View
from fastapi_users import schemas
from fastapi_users.db import BeanieBaseUser
from pydantic.fields import Field
from beanie.odm.documents import Document
from datetime import datetime

from app.schemas.category import Category
from app.schemas.ingredients import Ingredient
from app.schemas.review import Review
from app.schemas.recipe import Recipe


class User(BeanieBaseUser[PydanticObjectId]):
    avatar_url: Optional[str] = 'https://robohash.org/38'
    name: str = Field(...)
    biography: Optional[str] = Field(max_length=300)
    recipes: List[Link[Recipe]] = []
    followers: List[Link['User']] = []
    following: List[Link['User']] = []


class UserRead(schemas.BaseUser[PydanticObjectId]):
    avatar_url: Optional[str]
    name: Optional[str]
    biography: Optional[str]
    recipes: List[Link[Recipe]]
    followers: List[Link['User']]
    following: List[Link['User']]


class UserCreate(schemas.BaseUserCreate):
    name: str = Field(...)

    class Config:
        schema_extra = {
            'example': {
                'name': 'Geniuz',
                'email': 'tuffgniuz@dev.io',
                'password': '123456',
            }
        }


class UserUpdate(schemas.BaseUserUpdate):
    recipes: Optional[List[Link[Recipe]]]
