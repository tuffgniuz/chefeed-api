from array import array
from multiprocessing.dummy import Array
import uuid

from typing import Optional
from bson.objectid import ObjectId
from pydantic import BaseModel, Field
from datetime import date

from app.schemas.category import CategorySchema


class RecipeSchema(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    title: str = Field(...)
    description: str = Field(...)
    cooking_time: int = Field(...)
    image: Optional[str] = None  # path to image
    video: Optional[str] = None  # path to videofile
    created_at: date = Field(...)
    updated_at: Optional[date]
    # categories: Optional[list[CategorySchema]] = None
    # ingridient: Optional[list]  # (Dictionary,JSON,EMBEDDED,REFERENCE)
    # bookmarks: Optional[list]  # (Dictionary,Json,EMBEDDED,REFRENCE)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            'example': {
                'title': 'Mushroom Pizza',
                'description': 'Very Yummy Mushroom Pizza',
                'cooking_time': 10,
                'image': '',
                'video': '',
                'categories': '',
                'created_at': date.today()
            }  # Schema
        }


class RecipeUpdateSchema(BaseModel):
    title: Optional[str]
    description: Optional[str]
    cooking_time: Optional[int]
    attachment: Optional[str]
    create_at: Optional[date]
    update_at: Optional[date]
    #Category: Optional[array]
    #ingridients: Optional[array]
    #Bookmarks: Optional[array]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            'example': {
                'title': 'Mushroom Pizza',
                'description': 'Very Yummy Mushroom Pizza',
                'cooking_time': 10,
                'attachment': 'mushroompizza.jpg',
                'updated_at': date.today()
            }
        }
