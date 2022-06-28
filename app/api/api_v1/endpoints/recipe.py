# import json
from http import client
from beanie.odm.fields import PydanticObjectId, WriteRules
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from pymongo import MongoClient


from app.auth.login_manager import current_active_user
from app.schemas.recipe import Recipe
from app.schemas.users import User


router = APIRouter(prefix='/api/v1/recipes', tags=['Recipes'])

# For Aggregation Purposes
client = MongoClient("mongodb://root:root@127.0.0.1:27017/")
chefeed_db = client["chefeed-db"]
recipes = chefeed_db["recipes"]


@router.get('/', response_description='List all recipes')
async def retrieve_recipes() -> list[Recipe]:
    recipe_list = await Recipe.find().to_list()

    return recipe_list


@router.get('/user-recipes')
async def user_recipes(user: User = Depends(current_active_user)):
    await user.fetch_link(User.recipes)

    return user.recipes


@router.post('/new', response_description='Add new recipe')
async def create_recipe(recipe: Recipe, current_user=Depends(current_active_user)):
    new_recipe = await recipe.create()

    current_user.recipes.append(new_recipe)

    await current_user.save(link_rule=WriteRules.WRITE)


@router.put('/{id}', response_description='Update recipe')
async def update_recipe(id: PydanticObjectId, request: Recipe) -> Recipe:
    request = {key: value for key, value in recipe.dict().items()
               if value is not None}
    update_query = {'$set': {
        field: value for field, value in recipe.items()
    }}

    recipe = await Recipe.get(id)

    if not recipe:
        raise HTTPException(status_code=404, detail='Record not found')

    await recipe.update(update_query)

    return recipe


@router.get("/{id}", response_description="Show Recipe")
async def show_recipe(id: PydanticObjectId) -> Recipe:
    recipe = await Recipe.find_one(Recipe.id == id, fetch_links=True)
    if recipe is None:
        raise HTTPException(status_code=404, detail='Recipe not found')
    return recipe


@router.get("/{id}/Reviews", response_description="Show Recipe Reviews")
async def show_reviews_recipe(id: PydanticObjectId) -> Recipe:
    recipe = await Recipe.find_one(Recipe.id == id, fetch_links=True)
    recipe = recipe.reviews
    if recipe is None:
        return HTTPException(status_code=204, detail='No Reviews')
    return recipe
