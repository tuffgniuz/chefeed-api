from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Body
from pydantic import EmailStr
from starlette.requests import Request
from starlette.responses import JSONResponse
from .....config.settings import user_collection

from .....schemas.user import UserSchema, UserUpdateSchema
#from fastapi_users.router import get_oauth_router


router = APIRouter(prefix='/api/v1/auth',tags=['Authentication/Register'])

@router.post('/register',response_description='User Sign up',response_model=UserSchema)
async def sign_up(request:Request,user: UserSchema = Body(...)):
    #get username/email from inserted dict

    username = user.dict().get('username')
    email = user.dict().get('email')

    check_username = user_collection.find_one({"username":username})
    check_email = user_collection.find_one({"email":email})
   
    
    if check_username is not None:
        raise HTTPException(status_code=400,detail=f"Username existed")
    if check_email is not None:
        raise HTTPException(status_code=400,detail=f"Email existed")
    else:
        user = jsonable_encoder(user)
        new_user = await request.app.mongodb['users'].insert_one(user)
        created_user = await request.app.mongodb['users'].find_one({'_id': new_user.inserted_id})
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_user)
        