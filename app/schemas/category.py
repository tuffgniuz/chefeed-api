from array import array
from multiprocessing.dummy import Array
import uuid

from typing import Optional
from bson.objectid import ObjectId
from pydantic import BaseModel, Field
from datetime import date 

class CategorySchema(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    category_name: str = Field(...)
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            'example':{
                'category_name':'Vegetables',
            }
        }

class UpdateCategorySchema(BaseModel):
    category_name = Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            'example':{
                'category_name':'Vegetables',
            }
        }
    