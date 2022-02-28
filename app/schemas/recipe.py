from array import array
from multiprocessing.dummy import Array
import uuid

from typing import Optional
from bson.objectid import ObjectId
from pydantic import BaseModel, Field
from datetime import date 

class ReceipeSchema(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    title: str = Field(...)
    description: str = Field(...)
    cooking_time: int = Field(...)
    attachment: str = Field(...)
    create_at: date = Field(...)
    update_at: date = Field(...)
    category: array = Field(...)  #(Dictionary,Json,EMBEDDED,REFRENCE)
    ingridient: array = Field(...) #(Dictionary,JSON,EMBEDDED,REFERENCE)
    bookmarks: array = Field(...) #(Dictionary,Json,EMBEDDED,REFRENCE)

    class config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            'example':{
                'title':'Mushroom Pizza',
                'description':'Very Yummy Mushroom Pizza',
                'cooking_time': 10,
                'attachment': 'mushroompizza.jpg',
                'create_at':'2022-02-26',
                'update_at':'',
                'Category' : ["category_id","category_id2"],
                'Ingridients' : ["ingridients_id","ingridients_id2"],
                'Bookmarks' : ["bookmarks_id","bookmarks_id2"],
            }
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

        class config:
             arbitrary_types_allowed = True
             json_encoders = {ObjectId: str}
             schema_extra = {
            'example':{
                'title':'Mushroom Pizza',
                'description':'Very Yummy Mushroom Pizza',
                'cooking_time': 10,
                'attachment': 'mushroompizza.jpg',
                'create_at':'2022-02-26',
                'update_at':'',
                'Category' : ["category_id","category_id2"],
                'Ingridients' : ["ingridients_id","ingridients_id2"],
                'Bookmarks' : ["bookmarks_id","bookmarks_id2"],
            }
        }






    


