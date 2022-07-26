from app.auth.login_manager import current_active_user
from fastapi import APIRouter
from fastapi.param_functions import Depends
from beanie.odm.fields import PydanticObjectId, WriteRules, DeleteRules
from fastapi.exceptions import HTTPException


from app.schemas.review import Review
from app.schemas.recipe import Recipe

from tensorflow.keras.models import load_model 
from app.machine_learning.process_text import text_preprocessing

router = APIRouter(prefix='/api/v1/reviews', tags=["Reviews"])

<<<<<<< HEAD

@router.post('/{id}', response_description="Add Review to Recipe")
async def create_review(review: Review, id: PydanticObjectId, current_user=Depends(current_active_user)) -> dict:
=======
@router.get('/', response_description='List all reviews')
async def retrieve_reviews() -> list[Review]:
    # recipes = await request.app.mongodb['recipes'].find().to_list(1000)
    review_list = await Review.find().to_list()

    return review_list

@router.post('/{id}',response_description="Add Review to Recipe", status_code=200)
async def create_review(review:Review, recipe_id:PydanticObjectId, current_user = Depends(current_active_user)) -> dict:
    
    text = review.body
    word_count = len(text.replace(" ", "")) 

    if word_count > 150: 
        raise HTTPException(status_code=400, detail='Review must be shorter than 150 words!')

    text_processed = text_preprocessing(text)  
    model = load_model('/src/app/machine_learning/lstm_embed_tuned_valloss_ext2.h5') 
    pred = model.predict(text_processed)
    pred_sentiment = 'positive' 
    pred_score = float(pred[0,0])

    if pred_score < 0.5:  
        pred_sentiment = 'negative'
    
    review.predicted_sentiment = pred_sentiment
    review.sentiment_score = pred_score

>>>>>>> JovanAPIBeanieOwO
    new_review = await review.create()
    await new_review.save(link_rule=WriteRules.WRITE)


    recipe = await Recipe.get(recipe_id)

    if review is None:
        raise HTTPException(status_code=404, detail=f"Recipe does not exist with id {recipe_id}")

    recipe.reviews.append(new_review)
    await recipe.save(link_rule=WriteRules.WRITE)
<<<<<<< HEAD
=======


    current_user.reviews.append(new_review)
    await current_user.save(link_rule=WriteRules.WRITE) 

    return {"message: Review Added Successfully"}

@router.get("/{id}", response_description="Show Review")
async def show_review(id:PydanticObjectId) -> Review:
    review = await Review.find_one(Review.id==id,fetch_links=True)
    if review is None:
        raise HTTPException(status_code=404, detail='Review not found')
    return review



    
>>>>>>> JovanAPIBeanieOwO
