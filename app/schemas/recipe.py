import uuid

from typing import Optional, List
from beanie.odm.documents import Document
from beanie.odm.fields import Indexed, Link, PydanticObjectId
from bson.objectid import ObjectId
from pydantic import Field
from datetime import datetime, date

from app.schemas.category import Category
from app.schemas.ingredients import Ingredient
from app.schemas.review import Review
# from app.schemas.users import User

# from app.auth.login_manager import current_active_user

# class ReviewSchema(Document):
#     subject: str
#     description: str
#     created_date: date = Field(...)
#     updated_date: Optional[date] = Field(...)


# class IngredientsSchema(Document):
#     name: str
#     amount: int
#     measurement: str


# class CategorySchema(BaseModel):
#     categoryname: str


class Recipe(Document):
    # id: str = Field(default_factory=uuid.uuid4, alias='_id')
    title: str = Field(...)
    description: str = Field(max_length=350)
    cooking_time: int = Field(...)
    image_url: Optional[str] = 'https://img.freepik.com/free-vector/hand-drawn-nasi-lemak-food-illustrated_23-2148947678.jpg?t=st=1656305024~exp=1656305624~hmac=1686561aea3ace997594c4c61653f385f9997ca5a9d83a7b9e3e381ad6805ad3&w=826'
    categories: List[Link[Category]] = []
    ingredients: List[Link[Ingredient]] = []
    # user: Link[User]
    created_at: datetime = datetime.now()
    reviews: List[Link[Review]] = []
    # updated_at: Optional[date]
    # Category: List[CategorySchema]
    # Ingredients: List[IngredientsSchema]
    # Review: Optional[List[ReviewSchema]]

    class Settings:
        name = 'recipes'

    class Config:
        # allow_population_by_field_name = True
        # arbitrary_types_allowed = True
        schema_extra = {
            'example': {
                'title': '',
                'description': '',
                'cooking_time': 0,
                'image_url': 'https://img.freepik.com/free-vector/hand-drawn-nasi-lemak-food-illustrated_23-2148947678.jpg?t=st=1656305024~exp=1656305624~hmac=1686561aea3ace997594c4c61653f385f9997ca5a9d83a7b9e3e381ad6805ad3&w=826',
            }
        }

# class RecipeUpdateSchema(Document):
#     title: Optional[str]
#     description: Optional[str]
#     cooking_time: Optional[int]
#     attachment: Optional[str]
#     create_at: Optional[date]
#     update_at: Optional[date]
#     Category: Optional[list]
#     Ingridients: Optional[list]

#     class Config:
#         arbitrary_types_allowed = True
#         json_encoders = {ObjectId: str}
#         schema_extra = {
#             'example': {
#                 'title': '',
#                 'description': '',
#                 'cooking_time': 0,
#                 'attachment': '',
#                 'Category': [],
#                 'Ingredients': []
#             }
#         }
