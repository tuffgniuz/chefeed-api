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
    description: str = Field(...)
    created_at: date = Field(...)
    udpated_at: Optional[date]
    recipe: Optional[list]
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            'example':{
                'category_name':'Vegetables',
                'description':'Healthy Vegetables Food',
                'created_at': '2022-02-27',
            }
        }

class UpdateCategorySchema(BaseModel):
    category_name = Optional[str]
    description = Optional[str]
    created_at = Optional[date]
    updated_at = Optional[date]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            'example':{
                'category_name':'Vegetables',
                'description':'Healthy Vegetables Food',
                'created_at': '2022-02-27',
                'updated_at': '',
                'recipe': ["id","id2","id3"] #reference approach
            }
        }
    