from app.auth.login_manager import current_active_user
from fastapi import APIRouter
from fastapi.param_functions import Depends
from beanie.odm.fields import PydanticObjectId, WriteRules


from app.schemas.review import Review
from app.schemas.recipe import Recipe


router = APIRouter(prefix='/api/v1/reviews', tags=["Reviews"])


@router.post('/{id}', response_description="Add Review to Recipe")
async def create_review(review: Review, id: PydanticObjectId, current_user=Depends(current_active_user)) -> None:
    '''
    Creates a new review and links it to the corresponding recipe and user
    '''
    new_review = await review.create()
    new_review.user_id = current_user.id

    await new_review.save()

    recipe = await Recipe.get(id)

    recipe.reviews.append(new_review)

    await recipe.save(link_rule=WriteRules.WRITE)

    current_user.reviews.append(new_review)

    await current_user.save(link_rule=WriteRules.WRITE)
