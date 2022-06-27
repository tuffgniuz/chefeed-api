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
    # id : str = Field(default_factory=uuid.uuid4, alias='_id')
    # subject: str = Field(...)
    body: str = Field(...)
    created_at: datetime = datetime.now()
    updated_at: Optional[date]
    # user: Link[User]

    class Settings:
        name = 'reviews'

    class config:
        # allow_population_by_field_name = True
        # arbitrary_types_allowed = True
        schema_extra = {
            'example': {
                # 'subject': 'str',
                'body': 'str',
                # 'created_at': date.today()
            }
        }

# class UpdateReviewSchema(BaseModel):
#     subject = Optional[str]
#     description = Optional[str]
#     created_at = Optional[date]
#     updated_at = Optional[date]

#     class config:
#         arbitrary_types_allowed = True
#         json_encoders = {ObjectId: str}
#         schema_extra = {
#             'example':{
#                 'subject':'str',
#                 'description':'str',
#                 'updated_at': date.today()
#             }
#         }
