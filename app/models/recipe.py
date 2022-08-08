from typing import Optional
from beanie import Document, Link
from datetime import datetime
from pydantic import Field

from app.models.category import Category
from app.models.ingredient import Ingredient
from app.models.review import Review
# from app.models.user import User
# import app.models.user as user


class Recipe(Document):
    # user_id: Link[user.User]
    title: str = Field(...)
    cooking_time: int = Field(...)
    description: str = Field(...)
    image_url: str = Field(...)
    timestamp: datetime = datetime.now()

    category_id: Optional[Link[Category]]
    ingredient_ids: list[Link[Ingredient]] = []
    review_ids: list[Link[Review]] = []

    class Settings:
        name = 'recipes'

    class Config:
        schema_extra = {
            'example': {
                'title': 'Lamb Kebab',
                'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Pulvinar neque laoreet suspendisse interdum consectetur libero.',
                'cooking_time': 60,
                'image_url': 'https://images.pexels.com/photos/6416559/pexels-photo-6416559.jpeg?auto=compress&cs=tinysrgb&w=1600',
                # 'category_id': '',
            }
        }
