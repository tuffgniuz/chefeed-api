# from array import array
# from multiprocessing.dummy import Array
# import uuid

from typing import Optional
from beanie.odm.documents import Document
from beanie.odm.fields import Link
from bson.objectid import ObjectId
from pydantic import BaseModel, Field
from datetime import date, datetime

# from app.schemas.users import User


class Review(Document):
    body: str = Field(...)
    created_at: datetime = datetime.now()
    updated_at: Optional[date]

    class Settings:
        name = 'reviews'

    class config:
        schema_extra = {
            'example': {
                'body': 'str',
            }
        }
