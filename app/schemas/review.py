from array import array
from multiprocessing.dummy import Array
import uuid

from typing import Optional
from bson.objectid import ObjectId
from pydantic import BaseModel, Field
from datetime import date 


class ReviewSchema(BaseModel):
    id : str = Field(default_factory=uuid.uuid4, alias='_id')
    subject: str = Field(...)
    description: str = Field(...)
    created_at: date = Field(...)
    updated_at: Optional[date]

    class config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            'example':{
                'subject':'str',
                'description':'str',
                'created_at': date.today()
            }
        }

class UpdateReviewSchema(BaseModel):
    subject = Optional[str]
    description = Optional[str]
    created_at = Optional[date]
    updated_at = Optional[date]

    class config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            'example':{
                'subject':'str',
                'description':'str',
                'updated_at': date.today()
            }
        }
        

    
