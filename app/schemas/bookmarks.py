from datetime import date
import uuid

from typing import Optional
from bson.objectid import ObjectId
from pydantic import BaseModel, Field

class BookmarksSchema(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    name: str = Field(...)
    created_at: date = Field(...)
    updated_at: Optional[date]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            'example':{
                'name':'My Bookmark',
                'created_at': date.today()
            }
        }

class UpdateBookmarksSchema(BaseModel):
    name = Optional[str]
    created_at = Optional[date]
    updated_at = Optional[date]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            'example':{
                'name':'My Bookmark',
                'updated_at': date.today()
            }
        }