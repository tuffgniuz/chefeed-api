import json
from fastapi import APIRouter, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Body
from pydantic import ValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse

from ....config.settings import py_db
from ....loginmanager.loginmanager import get_current_active_user

from ....schemas.user import UserSchema
from ....schemas.recipe import RecipeSchema, RecipeUpdateSchema, ReviewSchema

router = APIRouter(prefix='/api/v1/recipes', tags=['Recipes'])


@router.get('/', response_description='List all recipes', response_model=list[RecipeSchema])
async def retrieve_recipes(request: Request):
    '''
    Takes a request a returns the recipe collection
        Parameters:
            request (Request): 

            Returns:
                recipes (Request): request list of recipe collection                
    '''
    recipes = await request.app.mongodb['recipes'].find().to_list(1000)

    return recipes


@router.get("/{id}", response_description="Get recipe by id")
async def retrieve_recipe_by_id(id: str, request: Request):
    '''
    Returns a single recipe from the recipe collection or raises an HTTPException
        Paramaters:
            id (str): the recipe id
            request (Request): a HTTP request
        Returns:
            recipe (document): A single recipe document of given id

    '''
    recipe = await request.app.mongodb["recipes"].find_one({"_id": id})
    if recipe is not None:
        return recipe
    raise HTTPException(
        status_code=404, detail=f"Recipe with {id} is not found")


@router.post('/new', response_description='Add new recipe', response_model=RecipeSchema)
async def create_recipe(request: Request, recipe: RecipeSchema = Body(...), current_user: UserSchema = Depends(get_current_active_user)):
    '''
    Returns a new recipe object
        Parameters:
            request (Request):
            recipe (RecipeScheme):
            current_user (UserSchema)
    '''
    recipe = jsonable_encoder(recipe)
    new_recipe = await request.app.mongodb['recipes'].insert_one(recipe)
    created_recipe = await request.app.mongodb['recipes'].find_one({'_id': new_recipe.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_recipe)


@router.delete("/delete/{id}", response_description="Delete Recipe")
async def delete_recipe(id: str, request: Request, current_user: UserSchema = Depends(get_current_active_user)):
    delete_recipe = await request.app.mongodb["recipes"].delete_one({"_id": id})
    if delete_recipe.deleted_count == 1:
        return "Recipe has been successfully deleted"
    raise HTTPException(
        status_code=404, detail=f"Recipe with {id} is not found")


@router.put('/update/{id}', response_description='Update a Receipe')
async def update_recipe(id: str, request: Request, recipe: RecipeUpdateSchema = Body(...), current_user: UserSchema = Depends(get_current_active_user)):
    recipe = {k: v for k, v in recipe.dict().items() if v is not None}
    if len(recipe) >= 1:
        update_result = await request.app.mongodb['recipes'].update_one({'_id': id}, {'$set': recipe})

        if update_result.modified_count == 1:
            if updated_recipe := await request.app.mongodb['recipes'].find_one({'_id': id}) is not None:
                return updated_recipe

    if (existing_recipe := await request.app.mongodb['recipes'].find_one({'_id': id})) is not None:
        return existing_recipe

    raise HTTPException(status_code=404, detail=f'Recipe {id} not found')


# REFERENCE JOIN BETWEEN DOCUMENTS

def ReviewToRecipe(review_id: str, recipe_id: str):
    review = py_db["categories"].find_one({'_id': review_id})
    result = py_db["recipe"].update_one(
        {'_id': recipe_id}, {'$push': {'Review': review}})
    return result


def CategoryToRecipe(category_id: str, recipe_id: str):
    category = py_db["categories"].find({'_id': category_id})
    result = py_db["recipe"].update_one(
        {'_id': recipe_id}, {'$push': {'Category': category}})
    return result


"""REVIEW ROUTERS INSIDE RECIPE"""


@router.get('/{id}/reviews', response_description='Show Recipe Reviews')
async def show_reviews(id: str, request: Request):
    recipe = await request.app.mongodb['recipes'].find_one({'_id': id})
    if recipe is not None:
        recipe_dict = recipe.dict()
        for i in recipe_dict.items():
            reviews = i[8]
        return reviews
    else:
        return HTTPException(status_code=404, detail=f'Recipe not Found')


@router.put('/{id}/post-review', response_description='Post a Review')
async def post_review(id: str, request: Request, review: ReviewSchema = Body(...)):
    recipe_count = py_db['recipes'].count({'_id': id})
    if recipe_count > 0:
        if py_db['recipes'].find_one({'recipes': id}) is not None:
            review = jsonable_encoder(review)
            new_review = await request.app.mongodb['reviews'].insert_one(review)
            created_review_to_recipe = ReviewToRecipe(
                new_review.inserted_id, id)
            return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_review_to_recipe)
        else:
            return HTTPException(status_code=404, detail=f'Recipe not Found')
    else:
        return HTTPException(status_code=404, detail=f'No Recipe existed')

# commend all ALT SHIFT A
