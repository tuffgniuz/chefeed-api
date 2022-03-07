from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Body
from starlette.requests import Request
from starlette.responses import JSONResponse

from ....schemas.ingredients import IngredientsSchema

router = APIRouter(prefix= '/api/v1/ingredients',tags=['ingredients'])

""" RETRIEVE ALL """
@router.get('/', response_description='List all ingredients', response_model=list[IngredientsSchema])
async def retrieve_ingredients(request: Request):
    ingredients = await request.app.mongodb['ingredients'].find().to_list(1000)

    return ingredients

""" RETRIEVE BY ID """
@router.get("/{id}", response_description="Get ingredients by id")
async def retrieve_ingredient_by_id(id: str, request: Request):
    ingridient = await request.app.mongodb["ingredients"].find_one({"_id": id})
    if ingridient is not None:
        return ingridient
    raise HTTPException(status_code=404, detail=f"ingredients with {id} is not found")

""" CREATE NEW """ 
@router.post('/', response_description='Add new ingridient', response_model=IngredientsSchema)
async def create_ingredient(request: Request, ingredient: IngredientsSchema = Body(...)):
    ingredient = jsonable_encoder(ingredient)
    new_ingredient = await request.app.mongodb['ingredients'].insert_one(ingredient)
    created_ingridient = await request.app.mongodb['ingredients'].find_one({'_id': new_ingredient.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_ingridient) 

""" DELETE BY ID """ 
@router.delete("/{id}", response_description="Delete Ingredients")
async def delete_ingredients(id: str, request: Request):
    delete_ingredient = await request.app.mongodb["ingredients"].delete_one({"_id": id})
    if delete_ingredient.deleted_count == 1:
        return "Ingredients has been successfully deleted"
    raise HTTPException(status_code=404, detail=f"Ingredients with {id} is not found")