import uuid

from typing import Optional
from bson.objectid import ObjectId
from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    name: str = Field(...)
    email: EmailStr = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            'example': {
                'name': 'Jane Doe',
                'email': 'jdoe@example.com'
            }
        }


class UserUpdateSchema(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            'example': {
                'name': "Jane Doe",
                'email': 'jdoe@example.com'
            }
        }
