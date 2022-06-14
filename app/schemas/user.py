import uuid

from typing import Optional,List
from bson.objectid import ObjectId
from pydantic import BaseModel, Field, EmailStr
from datetime import date
from fastapi_users import schemas

"""USERS SCHEMAS WITH FASTAPI"""

class BookmarkSchema(BaseModel):
    bookmarkname: str
    created_date: date

#class UserCreate(schemas.BaseUserCreate):
#    id: str = Field(default_factory=uuid.uuid4, alias='_id')
#    username: str = Field(...)
#    email: EmailStr = Field(...)
#    biography: Optional[str]
#    date_of_birth: date = Field(...)
    

#class UserUpdate(schemas.BaseUserUpdate):
#    email: Optional[EmailStr]
#    biography: Optional[str]
#    date_of_birth: Optional[date]
#    Bookmark : Optional[List[BookmarkSchema]]


#class UserRead(schemas.BaseUser[uuid.UUID]):
#    pass


class UserSchema(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    name: str = Field(...)
    email: EmailStr = Field(...)
    biography: Optional[str]
    date_of_birth: date = Field(...)
    Bookmark : List[BookmarkSchema]

class UserLoginSchema(BaseModel):
    username : str
    password : str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            'example': {
                'name': 'Jane Doe',
                'email': 'jdoe@example.com',
                'biography': 'I am Jane doe',
                'date_of_birth': '',
                'Bookmark':[]
            }
        }


class UserUpdateSchema(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    biography: Optional[str]
    date_of_birth: Optional[date]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            'example': {
                'name': '',
                'email': '',
                'biography': '',
                'date_of_birth': ''
            }
        }