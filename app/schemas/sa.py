from datetime import date
import uuid

from typing import Optional, List
from bson.objectid import ObjectId
from pydantic import BaseModel, Field

class SentimentAnalysisSchema(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    Review: Optional[List[str]]
    review_text: str = Field(...)
    review_sentiment: str = Field(...)
    # sentiment_score: float = Field(...)
    # predicted_sentiment: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            'example':{
                'review_text': 'Food is not that good',
                'review_sentiment': 'positive'
            }
        }

class PredictSentimentAnalysisSchema(BaseModel):
    Review: Optional[List[str]]
    review_text = Optional[str]
    review_sentiment = Optional[str]
    sentiment_score = Optional[float]
    predicted_sentiment = Optional[str]


    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            'example':{
                'review_text':'Food is not that good',
                'review_sentiment': 'positive',
                'sentiment_score': 0.6890,
                'predicted_sentiment': 'negative'
            }
        }