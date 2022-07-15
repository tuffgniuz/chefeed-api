from typing import List, Optional
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


@router.post('/new', response_description='Add new recipe')
async def create_recipe(
    ing: List[PydanticObjectId],
    # category_id: PydanticObjectId,
    recipe: Recipe,
    current_user=Depends(current_active_user)
) -> None:
    '''Create new recipe for current user'''
    new_recipe = await recipe.create()
    # new_recipe.user_id = current_user.id
    # await new_recipe.save()  # update new recipe with user id added

    for ingredient in ing:
        list_of_ingredient = await Ingredient.find_one(Ingredient.id == ingredient)
        new_recipe.ingredients.append(list_of_ingredient)

    # category = await Category.find_one(Category.id == category_id)
    # new_recipe.categories.append(category)

    await new_recipe.save(link_rule=WriteRules.WRITE)

    current_user.recipes.append(new_recipe)

    await current_user.save(link_rule=WriteRules.WRITE)


@router.get('/query', response_description='Find recipe ')
async def find_recipes(recipe_title: Optional[str]) -> list[Recipe]:
    result = await Recipe.find(Recipe.title == recipe_title).to_list()

    return result


@router.get('/', response_description='List all recipes')
async def get_recipes() -> list[Recipe]:
    '''
    Get all recipes
    '''
    recipe_list = await Recipe.find().to_list()
    # recipe_list = await Recipe.find

    return recipe_list


@router.get('/users/{id}', response_description='Get User with Links')
async def get_user_recipes(id: PydanticObjectId):
    '''
    Fetched the recipes with Links from the user
    '''
    user_recipes = await User.find_one(User.id == id, fetch_links=True)

    return user_recipes


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
