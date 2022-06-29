from fastapi import APIRouter
from fastapi.params import Depends
from beanie.odm.fields import PydanticObjectId, WriteRules

from app.auth.login_manager import current_active_user
from app.schemas.users import User
from ....schemas.category import Category
from ....schemas.recipe import Recipe

router = APIRouter(prefix='/api/v1/categories', tags=['Categories'])


@router.get('/', response_description='List All Categories')
async def retrieve_category() -> list[Category]:
    '''
    Return a list of all categories
    '''
    categories = await Category.find().to_list()

    return categories


@router.get('/{id}', response_description='Query for a category')
async def query_category(id: PydanticObjectId):
    category = await Category.get(id)

    return category


@router.post('/create', response_description='Add new category')
async def create_category(category: Category, current_user: User = Depends(current_active_user)):
    '''
    Inserts a new category
    '''
    await category.create()


# @router.post('/{id}', response_description="Add Category to Recipe")
# async def add_ingredients_to_recipe(id: PydanticObjectId, category_id: PydanticObjectId, current_user=Depends(current_active_user)) -> dict:
#     recipe = await Recipe.get(id)
#     category = await Category.find_one(Category.id == category_id)
#     recipe.categories.append(category)
#     await recipe.save(link_rule=WriteRules.WRITE)
