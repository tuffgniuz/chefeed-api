from typing import Optional
from beanie import Document
from pydantic import Field


class Ingredient(Document):
    name: str = Field(...)
    icon_url: Optional[str]

    class Settings:
        name = 'ingredients'

    class Config:
        schema_extra = {
            'example': {
                'name': 'Garlic',
            }
        }
