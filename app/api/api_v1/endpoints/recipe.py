from http import client
from typing import List
from beanie.odm.fields import PydanticObjectId, WriteRules
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends

from app.auth.login_manager import current_active_user
from app.schemas.category import Category
from app.schemas.ingredients import Ingredient
from app.schemas.recipe import Recipe
from app.schemas.users import User
from app.schemas.ingredients import Ingredient
from app.schemas.category import Category


router = APIRouter(prefix='/api/v1/recipes', tags=['Recipes'])


@router.get('/', response_description='List all recipes')
async def get_recipes() -> list[Recipe]:
    '''
    Get all recipes
    '''
    recipe_list = await Recipe.find().to_list()

    return recipe_list


@router.get('/u/{id}', response_description='Retrieves the users created recipe')
async def get_user_recipes(id: PydanticObjectId, user: User = Depends(current_active_user)):
    '''
    Fetched the recipes with Links from the user
    '''
    await user.fetch_link(User.recipes)

    return user.recipes


@router.post('/new', response_description='Add new recipe')
async def create_recipe(
        recipe: Recipe,
        ingredient_ids: list[PydanticObjectId],
        current_user=Depends(current_active_user)):
    '''
    Creates a new recipe object and appends to the list of the user recipe list
    '''
    new_recipe = await recipe.create()

    for ingredient_id in ingredient_ids:
        ingredient = await Ingredient.find_one(Ingredient.id == ingredient_id)
        new_recipe.ingredients.append(ingredient)

    await new_recipe.save(link_rule=WriteRules.WRITE)


async def create_recipe(ing: List[PydanticObjectId], category_id: PydanticObjectId, recipe: Recipe, current_user=Depends(current_active_user)) -> dict:
    new_recipe = await recipe.create()

    for ingredient in ing:
        list_of_ingredient = await Ingredient.find_one(Ingredient.id == ingredient)
        new_recipe.ingredients.append(list_of_ingredient)

    category = await Category.find_one(Category.id == category_id)
    new_recipe.categories.append(category)

    await new_recipe.save(link_rule=WriteRules.WRITE)

    current_user.recipes.append(new_recipe)

    await current_user.save(link_rule=WriteRules.WRITE)


@router.get("/{id}", response_description="Show Recipe")
async def get_recipe_by_id(id: PydanticObjectId) -> Recipe:
    '''
    Get single recipe and its Links by given id

        Parameters:
            id (PydanticObjectId): the recipe object id
    '''
    recipe = await Recipe.find_one(Recipe.id == id, fetch_links=True)
    if recipe is None:
        raise HTTPException(status_code=404, detail='Recipe not found')
    return recipe


@router.put('/{id}', response_description='Update recipe')
async def update_recipe(id: PydanticObjectId, request: Recipe) -> Recipe:
    '''
    Retuns an updated recipe object
    '''
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


@router.get("/{id}/reviews", response_description='Retrieves recipe reviews from given recipe by {_id}')
async def get_recipe_reviews_by_id(id: PydanticObjectId) -> Recipe:
    '''
    Get reviews from recipe by id
    '''
    recipe = await Recipe.find_one(Recipe.id == id, fetch_links=True)
    recipe_reviews = recipe.reviews
    if recipe_reviews is None:
        return HTTPException(status_code=204, detail='No Reviews')
    return recipe_reviews
