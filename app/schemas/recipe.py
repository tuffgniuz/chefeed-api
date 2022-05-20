#from array import array
#from multiprocessing.dummy import Array
import uuid

from typing import Optional,List
from bson.objectid import ObjectId
from pydantic import BaseModel, Field
from datetime import date 

class IngredientsSchema(BaseModel):
    name: str 
    icon: str


class RecipeSchema(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    title: str = Field(...)
    description: str = Field(...)
    cooking_time: int = Field(...)
    attachment: str = Field(...)
    Category: List[str] = [] #(list,Json,EMBEDDED,REFRENCE)
    Ingredients: List[IngredientsSchema] = [] #(list,JSON,EMBEDDED,REFERENCE)


    class Config: 
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            'example':{
                'title':'',
                'description':'',
                'cooking_time': 0,
                'attachment': '',
                'category' : [],
                'ingredients' : [
                    {'name' : '',
                    'icon': ''}
                ]
            } #Schema 
        }
    
class RecipeUpdateSchema(BaseModel):
    title: Optional[str]
    description: Optional[str]
    cooking_time: Optional[int]
    attachment: Optional[str]
    create_at: Optional[date]
    update_at: Optional[date]
    Category: Optional[list]
    Ingridients: Optional[list]


    class Config:
            arbitrary_types_allowed = True
            json_encoders = {ObjectId: str}
            schema_extra = {
        'example':{
            'title':'',
            'description':'',
            'cooking_time': 0,
            'attachment': '',
            'Category' : [],
            'Ingredients' : []
        }
    }






    


