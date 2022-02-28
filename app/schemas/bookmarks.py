from datetime import date
import uuid

from typing import Optional
from bson.objectid import ObjectId
from pydantic import BaseModel, Field

class BookmarksSchema(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    name: str = Field(...)
    created_at: date = Field(...)
    updated_at: date = Field(...)

    class config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            'example':{
                'name':'My Bookmark',
                'created_at':'2022-02-27',
                'updated_at':''
            }
        }

class UpdateBookmarksSchema(BaseModel):
    name = Optional[str]
    created_at = Optional[date]
    updated_at = Optional[date]

    class config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            'example':{
                'name':'My Bookmark',
                'created_at':'2022-02-27',
                'updated_at':''
            }
        }