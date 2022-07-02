from distutils.command.install_egg_info import safe_name
from fastapi import APIRouter, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Body
from starlette.requests import Request
from starlette.responses import JSONResponse
from tensorflow.keras.models import load_model 
import tensorflow as tf
import numpy as np

from app.schemas.sa import SentimentAnalysisSchema, PredictSentimentAnalysisSchema
from app.machine_learning.process_text import text_preprocessing

router = APIRouter(prefix='/api/v1/sentimentanalysis',tags=['SentimentAnalysis'])

# """RETRIEVE ALL SA"""
# @router.get('/',response_description='List all sa' ,response_model=list[SentimentAnalysisSchema],)
# async def retrieve_sa(request:Request):
#     sa = await request.app.mongodb['sa'].find().to_list(1000)
#     return sa

"""PREDICT SENTIMENT"""
@router.post('/',response_description='Predict Sentiment', response_model=SentimentAnalysisSchema)
async def create_sa(request:Request, sa:SentimentAnalysisSchema  = Body(...)):
    sa = jsonable_encoder(sa)

    text_processed = text_preprocessing(sa['review_text'])
    model = load_model('/src/app/machine_learning/gru_embed.h5')
    pred = model.predict(text_processed)
    predicted_sentiment = 'positive' 
    pred_score = float(pred[0,0])

    if pred_score < 0.5:  
        predicted_sentiment = 'negative'

    sa['predicted_sentiment'] = predicted_sentiment
    sa['sentiment_score'] = pred_score
 
    new_sa = await request.app.mongodb['sentimentanalysis'].insert_one(sa)
    created_sa = await request.app.mongodb['sentimentanalysis'].find_one({'_id':new_sa.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_sa)



