from unicodedata import category
from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Body
from fastapi.params import Depends
from starlette.requests import Request
from starlette.responses import JSONResponse
from beanie.odm.fields import PydanticObjectId,WriteRules

from app.auth.login_manager import current_active_user
from ....schemas.category import Category
from ....schemas.recipe import Recipe

router = APIRouter(prefix='/api/v1/categories', tags=['Categories'])


@router.get('/', response_description='List All Categories')
async def retrieve_category() -> list[Category]:
    '''Return a list of all categories'''
    # categories = await request.app.mongodb['categories'].find().to_list(1000)
    categories = await Category.find().to_list()
    return categories


# @router.get("/{id}", response_description="Get cateogry by id")
# async def retrieve_category_by_id(id: str, request: Request):
#     '''Return a single category by given Id'''
#     category = await request.app.mongodb["categories"].find_one({"_id": id})
#     if category is not None:
#         return category
#     raise HTTPException(
#         status_code=404, detail=f"Category with {id} is not found")


@router.post('/', response_description='Add new category')
async def create_category(category: Category, current_user=Depends(current_active_user)):
    '''Inserts a new category'''
    # category = jsonable_encoder(category)
    # new_category = await request.app.mongodb['categories'].insert_one(category)
    # created_category = await request.app.mongodb['categories'].find_one({'_id': new_category.inserted_id})
    # return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_category)
    await category.create()

""" @router.post('/{id}',response_description="Add Category to Recipe")
async def add_ingredients_to_recipe(id:PydanticObjectId, category_id: PydanticObjectId, current_user = Depends(current_active_user)) -> dict:
    recipe = await Recipe.get(id)
    category = await Category.find_one(Category.id == category_id)
    recipe.categories.append(category)
    await recipe.save(link_rule=WriteRules.WRITE) """

# @router.delete("/{id}", response_description="Delete category")
# async def delete_category(id: str, request: Request):
#     delete_category = await request.app.mongodb["categories"].delete_one({"_id": id})
#     if delete_category.deleted_count == 1:
#         return "Category has been successfully deleted"
#     raise HTTPException(
#         status_code=404, detail=f"Category with {id} is not found")
#
