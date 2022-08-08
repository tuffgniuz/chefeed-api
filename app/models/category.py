from beanie import Document
from pydantic import Field


class Category(Document):
    name: str = Field(...)

    class Settings:
        name = 'categories'

    class Config:
        schema_extra = {
            'example': {
                'name': 'Middle Eastern'
            }
        }
