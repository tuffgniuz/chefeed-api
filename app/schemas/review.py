# from array import array
# from multiprocessing.dummy import Array
# import uuid

from typing import Optional
from beanie.odm.documents import Document
from beanie.odm.fields import PydanticObjectId, Link
from pydantic import Field
from datetime import date, datetime

# from app.schemas.users import User
# import app.schemas.users as users
# import app.schemas.users


class Review(Document):
    # user_id: Link[app.schemas.users]
    body: str = Field(...)
    created_at: datetime = datetime.now()
    updated_at: Optional[date]

    class Settings:
        name = 'reviews'

    class Config:
        schema_extra = {
            'example': {
                'body': 'str',
            }
        }
