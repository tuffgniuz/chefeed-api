from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from ....crud.crud_user import create_user, retrieve_users
from ....schemas.user import ResponseModel, UserSchema

router = APIRouter(prefix='/api/v1/users', tags=['users'])


@router.get('/', response_description='Users retrieved')
async def get_users():
    users = await retrieve_users()

    if users:
        return ResponseModel(users, 'Users revietreved successfully')

    return ResponseModel(users, 'Empty list retrieved')


@router.post('/create')
async def add_user(user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    new_user = await create_user(user)

    return ResponseModel(new_user, 'User object added to collection')
