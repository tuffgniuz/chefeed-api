from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Body
from starlette.requests import Request
from starlette.responses import JSONResponse
from .....schemas.user import UserLoginSchema,UserSchema,UserInDB,Token
from .....loginmanager.loginmanager import (get_current_active_user,authenticate_user,ACCESS_TOKEN_EXPIRE_MINUTES,create_access_token)
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix='/api/v1/token',tags=["LOGIN"])


@router.post('/token',response_model=Token)
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