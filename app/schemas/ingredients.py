#from array import array
from multiprocessing.dummy import Array
#from tkinter import BitmapImage
import uuid

from typing import Optional
from bson.objectid import ObjectId
from pydantic import BaseModel, Field
from datetime import date 

class IngredientsSchema(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    name : str = Field(...)
    created_at: date = Field(...)
    updated_at: Optional[date]
    icon: Optional[str]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            'example':{
                'name' : 'Sugar',
                'created_at': date.today(),
                }
            }

class UpdateIngredientsSchema(BaseModel):
    name = Optional[str]
    created_at = Optional[date]
    updated_at = Optional[date]
    icon = Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            'example':{
                'name' : '',
                'updated_at': date.today(),
            }
        }