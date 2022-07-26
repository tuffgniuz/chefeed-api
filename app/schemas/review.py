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
    # user: Link[User]
    predicted_sentiment: Optional[str]
    sentiment_score: Optional[float]

    class Settings:
        name = 'reviews'

    class Config:
        schema_extra = {
            'example': {
                'body': 'str',
            }
        }
