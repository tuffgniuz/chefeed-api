from beanie import PydanticObjectId, WriteRules
from fastapi import APIRouter, Depends
from app.models.category import Category

from app.api.auth.login_manager import current_active_user
from app.models.recipe import Recipe
from app.models.user import User


router = APIRouter(prefix='/api/v1/recipes', tags=['recipes'])


@router.get('/', response_description='Get all recipes')
async def get_recipes() -> list:
    '''
    Return all recipes and its related documents
    '''
    recipes = await Recipe.find(fetch_links=True).to_list()

    return recipes


@router.get('/{id}', response_description='Get one recipe')
async def get_recipe_by_id(id: PydanticObjectId):
    '''
    Return one recipe and its related documents
    '''
    recipe = await Recipe.get(id, fetch_links=True)

    return recipe


@router.post('/new', response_description='Post new recipe')
async def post_recipe(category_id: PydanticObjectId, recipe: Recipe, current_user: User = Depends(current_active_user)):
    '''
    Post new recipe
    '''
    category = await Category.get(category_id)
    recipe.category_id = category
    new_recipe = await recipe.create()

    current_user.recipe_ids.append(new_recipe)
    await current_user.save(link_rule=WriteRules.WRITE)
