from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Body
from starlette.requests import Request
from starlette.responses import JSONResponse

from ....schemas.category import CategorySchema

router = APIRouter(prefix= '/api/v1/categories',tags=['categories'])

"""RETRIEVE ALL CATEGORY"""
@router.get('/', response_description = 'List All Categories',response_model=list[CategorySchema])
async def retrieve_category(request: Request):
    categories = await request.app.mongodb['categories'].find().to_list(1000)
    return categories


"""RETRIEVE CATEGORY BY ID"""
@router.get("/{id}", response_description="Get cateogry by id")
async def retrieve_category_by_id(id: str, request: Request):
    category = await request.app.mongodb["categories"].find_one({"_id": id})
    if category is not None:
        return category
    raise HTTPException(status_code=404, detail=f"Category with {id} is not found")


"""CREATE NEW CATEGORY"""
@router.post('/', response_description='Add new category', response_model=CategorySchema)
async def create_category(request: Request, category: CategorySchema = Body(...)):
    category = jsonable_encoder(category)
    new_category = await request.app.mongodb['categories'].insert_one(category)
    created_category = await request.app.mongodb['categories'].find_one({'_id': new_category.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_category) 

""" DELETE CATEGORY ID """ 
@router.delete("/{id}", response_description="Delete category")
async def delete_category(id: str, request: Request):
    delete_category = await request.app.mongodb["categories"].delete_one({"_id": id})
    if delete_category.deleted_count == 1:
        return "Category has been successfully deleted"
    raise HTTPException(status_code=404, detail=f"Category with {id} is not found")
