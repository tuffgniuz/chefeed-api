
from fastapi import APIRouter

from app.models.category import Category

router = APIRouter(prefix='/api/v1/categories', tags=['categories'])


@router.get('/', response_description='Get all categories')
async def get_categories() -> list:
    '''Return all categories'''
    categories = await Category.find().to_list()
    return categories


@router.post('/new', response_description='Post new category')
async def post_category(category: Category):
    await category.create()
