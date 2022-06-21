import uuid

from typing import Optional,List
from bson.objectid import ObjectId
from pydantic import BaseModel, Field, EmailStr
from datetime import date
#import nltk

"""USERS SCHEMAS WITH FASTAPI"""

class BookmarkSchema(BaseModel):
    bookmarkname: str
    created_date: date

# Register/User Schema
class UserSchema(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    username: str = Field(...)
    email: EmailStr = Field(...)
    biography: Optional[str]
    date_of_birth: date  = Field(...)
    Bookmark : Optional[List[BookmarkSchema]]
    #Recipe: Optional[List[str]]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            'example': {
                'username': 'string',
                'email': 'Email@example.com',
                'biography': 'Insert your Biography Here',
                'date_of_birth': 'Insert date of birth here'
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
                'username': '',
                'email': '',
                'biography': '',
                'date_of_birth': ''
            }
        }

#User Login Schemas
class UserLoginSchema(BaseModel):
    username : str
    password : str

class UserInDB(UserSchema):
    hashed_password = str

class Token(BaseModel):
    access_token : str
    token_type : str
    name: str

class TokenData(BaseModel):
    username: Optional[str] = None

def get_user(db,username:str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


#schemas.BaseUserCreate
class UserCreate(BaseModel):
    username: str = Field(...)
    password: str = Field(...)
    email: EmailStr = Field(...)
    biography: Optional[str]
    date_of_birth: date = Field(...)
    
#schemas.BaseUser[uuid.UUID]
class UserRead(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    username: str = Field(...)
    email: EmailStr = Field(...)
    biography: Optional[str]
    date_of_birth: date = Field(...)
    Bookmark : Optional[List[BookmarkSchema]]