#from fastapi import APIRouter, status
#from fastapi.encoders import jsonable_encoder
#from fastapi.exceptions import HTTPException
#from fastapi.param_functions import Body
#from starlette.requests import Request
#from starlette.responses import JSONResponse
#from .....schemas.user import UserCreate

#router = APIRouter(prefix='/api/v1/userauth/jwt',tags=["userauth"])

#@router.post('/login',response_model="User Login")
#async def user_login(username:str,password:str):
#    pass

#@router.post('/logoff',response_model="User Log Off")
#async def user_logoff():
#    pass
