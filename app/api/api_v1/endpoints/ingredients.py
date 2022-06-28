from beanie import PydanticObjectId
from beanie.odm.fields import WriteRules
from fastapi import APIRouter, status
from fastapi.params import Depends
# from fastapi.encoders import jsonable_encoder
# from fastapi.exceptions import HTTPException
# from fastapi.param_functions import Body
# from starlette.requests import Request
# from starlette.responses import JSONResponse

from app.auth.login_manager import current_active_user
from ....schemas.ingredients import Ingredient
from ....schemas.recipe import Recipe

router = APIRouter(prefix='/api/v1/ingredients', tags=['Ingredients'])


@router.get('/', response_description='List all ingredients')
async def retrieve_ingredients() -> list[Ingredient]:
    '''Returns a list of all ingredients'''
    # ingredients = await request.app.mongodb['ingredients'].find().to_list(1000)
    ingredients = await Ingredient.find().to_list()

    return ingredients

# """ RETRIEVE BY ID """
# @router.get("/{id}", response_description="Get ingredients by id")
# async def retrieve_ingredient_by_id(id: str, request: Request):
#     ingridient = await request.app.mongodb["ingredients"].find_one({"_id": id})
#     if ingridient is not None:
#         return ingridient
#     raise HTTPException(status_code=404, detail=f"ingredients with {id} is not found")


@router.post('/new', response_description='Add new ingridient')
async def create_ingredient(ingredient: Ingredient, current_user=Depends(current_active_user)):
    '''Creates a new ingredient'''
    # ingredient = jsonable_encoder(ingredient)
    # new_ingredient = await request.app.mongodb['ingredients'].insert_one(ingredient)
    # created_ingridient = await request.app.mongodb['ingredients'].find_one({'_id': new_ingredient.inserted_id})
    # return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_ingridient)
    await ingredient.create()


@router.post('/{id}',response_description="Add Ingredients to Recipe")
async def add_ingredients_to_recipe(id:PydanticObjectId, ingredients_id: PydanticObjectId, current_user = Depends(current_active_user)) -> dict:
    recipe = await Recipe.get(id)
    ingredients = await Ingredient.find_one(Ingredient.id == ingredients_id)
    recipe.ingredients.append(ingredients)
    await recipe.save(link_rule=WriteRules.WRITE)

#

# """ DELETE BY ID """
# @router.delete("/{id}", response_description="Delete Ingredients")
# async def delete_ingredients(id: str, request: Request):
#     delete_ingredient = await request.app.mongodb["ingredients"].delete_one({"_id": id})
#     if delete_ingredient.deleted_count == 1:
#         return "Ingredients has been successfully deleted"
#     raise HTTPException(status_code=404, detail=f"Ingredients with {id} is not found")
