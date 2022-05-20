import json
from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Body
from starlette.requests import Request
from starlette.responses import JSONResponse

from ....schemas.recipe import RecipeSchema, RecipeUpdateSchema
from ....schemas.ingredients import IngredientsSchema,UpdateIngredientsSchema
from ....schemas.category import CategorySchema, UpdateCategorySchema

router = APIRouter(prefix='/api/v1/recipes', tags=['recipes'])

""" RETRIEVE ALL """
@router.get('/', response_description='List all recipes', response_model=list[RecipeSchema])
async def retrieve_recipes(request: Request):
    recipes = await request.app.mongodb['recipes'].find().to_list(1000)

    return recipes

""" RETRIEVE BY ID """
@router.get("/{id}", response_description="Get recipe by id")
async def retrieve_recipe_by_id(id: str, request: Request):
    recipe = await request.app.mongodb["recipes"].find_one({"_id": id})
    if recipe is not None:
        return recipe
    raise HTTPException(status_code=404, detail=f"Recipe with {id} is not found")

""" CREATE NEW """   
@router.post('/', response_description='Add new recipe', response_model=RecipeSchema)
async def create_recipe(request: Request, recipe: RecipeSchema = Body(...)):
    recipe = jsonable_encoder(recipe)
    new_recipe = await request.app.mongodb['recipes'].insert_one(recipe)
    created_recipe = await request.app.mongodb['recipes'].find_one({'_id': new_recipe.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_recipe) 

""" DELETE BY ID """ 
@router.delete("/{id}", response_description="Delete Recipe")
async def delete_recipe(id: str, request: Request):
    delete_recipe = await request.app.mongodb["recipes"].delete_one({"_id": id})
    if delete_recipe.deleted_count == 1:
        return "Recipe has been successfully deleted"
    raise HTTPException(status_code=404, detail=f"Recipe with {id} is not found")

"""UPDATE BY ID"""
@router.put('/{id}', response_description='Update a Receipe')
async def update_recipe(id: str, request:Request, recipe: RecipeUpdateSchema = Body(...)):
    recipe = {k:v for k,v in recipe.dict().items() if v is not None}
    if len(recipe) >= 1:
        update_result = await request.app.mongodb['recipes'].update_one({'_id':id},{'$set': recipe})

        if update_result.modified_count == 1:
            if updated_recipe := await request.app.mongodb['recipes'].find_one({'_id': id}) is not None:
                return updated_recipe

    if (existing_recipe:= await request.app.mongodb['recipes'].find_one({'_id': id})) is not None:
        return existing_recipe
    
    raise HTTPException(status_code=404, detail=f'Recipe {id} not found')





