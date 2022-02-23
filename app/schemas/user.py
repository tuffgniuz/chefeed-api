from typing import Optional
from pydantic import Field, EmailStr
from fastapi_users.models import (
    # BaseUser,
    BaseUser,
    BaseUserCreate,
    BaseUserDB,
    BaseUserUpdate
)


class UserCreate(BaseUserCreate):
    pass
    # id: str = Field(default_factory=uuid.uuid4, alias='_id')
    # name: str = Field(...)
    # avatar_url: Optional[str] = None

    # class Config:
    #     allow_population_by_field_name = True
    #     arbitrary_types_allowed = True
    #     schema_extra = {
    #         'example': {
    #             'name': 'Jane Doe',
    #             'email': 'jdoe@example.com'
    #         }
    # }


class UserUpdate(BaseUserUpdate):
    pass
    # name: Optional[str]

    # class Config:
    #     arbitrary_types_allowed = True
    #     json_encoders = {ObjectId: str}
    #     schema_extra = {
    #         'example': {
    #             'name': "Jane Doe",
    #             'email': 'jdoe@example.com'
    #         }
    #     }


class User(BaseUser):
    pass
    # name: str
    # avatar_url: str


class UserDisplay(BaseUserDB):
    pass
    # name: str
    # email: str
    # avatar_url: str
