import uuid

from typing import Optional
from bson.objectid import ObjectId
from pydantic import BaseModel, Field, EmailStr
from datetime import date


class UserSchema(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    name: str = Field(...)
    email: EmailStr = Field(...)
    biography: Optional[str]
    date_of_birth: date = Field(...)
    created_at: date.today()
    updated_at: Optional[date]



    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            'example': {
                'name': 'Jane Doe',
                'email': 'jdoe@example.com',
                'biography': 'I am Jane doe'
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
                'name': "Jane Doe",
                'email': 'jdoe@example.com'
            }
        }
