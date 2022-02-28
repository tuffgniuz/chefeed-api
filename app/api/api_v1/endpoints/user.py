from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Body
from starlette.requests import Request
from starlette.responses import JSONResponse

from ....schemas.user import UserSchema, UserUpdateSchema
# from ....config.settings import database as db


router = APIRouter(prefix='/api/v1/users', tags=['users'])


@router.get('/', response_description='List all users', response_model=list[UserSchema])
async def retrieve_users(request: Request):
    users = await request.app.mongodb['users'].find().to_list(1000)

    return users


@router.post('/', response_description='Add new user', response_model=UserSchema)
async def create_user(request: Request, user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    new_user = await request.app.mongodb['users'].insert_one(user)
    created_user = await request.app.mongodb['users'].find_one({'_id': new_user.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_user)


@router.put('/{id}', response_description='Update a user')
async def update_user(id: str, request: Request, user: UserUpdateSchema = Body(...)):
    user = {k: v for k, v in user.dict().items() if v is not None}

    if len(user) >= 1:
        update_result = await request.app.mongodb['users'].update_one({'_id': id}, {'$set': user})

        if update_result.modified_count == 1:
            if updated_user := await request.app.mongodb['users'].find_one({'_id': id}) is not None:
                return updated_user

    if (existing_user := await request.app.mongodb['users'].find_one({'_id': id})) is not None:
        return existing_user

    raise HTTPException(status_code=404, detail=f'user {id} not found')