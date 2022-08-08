
from datetime import datetime
from typing import Optional
from beanie import Document
from pydantic import Field


class Review(Document):
    body: str = Field(...)
    created_at: datetime = datetime.now()
    predicted_sentiment: Optional[str]
    sentiment_score: Optional[str]

    class Settings:
        name = 'reviews'

    class Config:
        schema_extra = {
            'example': {
                'body': 'One of the best recipes I have tried!'
            }
        }
