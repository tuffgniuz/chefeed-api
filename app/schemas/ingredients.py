from multiprocessing.dummy import Array
#from tkinter import BitmapImage
import uuid

from typing import Optional
from bson.objectid import ObjectId
from pydantic import BaseModel, Field


class IngredientsSchema(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    name : str = Field(...)
    measurement : str = Field(...)
    amount: int = Field(...)
    icon: Optional[str]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            'example':{
                'name' : 'str',
                'measurement': 'str',
                'amount':'',
                'icon':'str',
                }
            }

class UpdateIngredientsSchema(BaseModel):
    name = Optional[str]
    measurement = Optional[str]
    amount = Optional[int]
    icon = Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            'example':{
                'name' : 'Sugar',
                'measurement': 'str',
                'amount':'',
                'icon':'str',
            }
        }