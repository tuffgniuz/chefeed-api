from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Body
from starlette.requests import Request
from starlette.responses import JSONResponse
from .....schemas.user import UserLoginSchema,UserSchema,UserInDB,Token
from .....loginmanager.loginmanager import (get_current_active_user,authenticate_user,ACCESS_TOKEN_EXPIRE_MINUTES,create_access_token)
from fastapi.security import OAuth2PasswordRequestForm
from .....config.settings import user_collection


router = APIRouter(prefix='/api/v1/auth',tags=['Authentication/Register'])
#router = APIRouter(prefix='/api/v1/token',tags=["LOGIN"])

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
        

#@router.post('/token',response_model=Token)
@router.post('/login', response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username,form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"User CheFeed Not Authorized",
        headers={"WWW-Authenticate": "Bearer"},)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data=
        {
            "username":user.username,
            "name": user.name
        }, expires_delta=access_token_expires
    ) 
    return
    {
         {
        "access_token": access_token, 
        "token_type": "bearer",
        "name": user.name,
        }
    }

@router.post("/forget-password",response_description="Forget Password")
async def forget_password():
    return "Forget Password"

