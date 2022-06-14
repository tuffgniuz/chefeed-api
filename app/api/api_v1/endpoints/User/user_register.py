#from fastapi import APIRouter, status
#from fastapi.encoders import jsonable_encoder
#from fastapi_users import BaseUserManager
#from fastapi.exceptions import HTTPException
#from fastapi.param_functions import Body
#from starlette.requests import Request
#from starlette.responses import JSONResponse
#from fastapi_users import BaseUserManager
#from .....schemas.user import UserCreate, UserRead


#router = APIRouter(prefix='/api/v1/userregister',tags=["userregister"])

#@router.post('/register',response_model="User Sign Up")
#async def user_registeration(request:Request , user: UserCreate = Body()):
#    user = jsonable_encoder(user)
    #existing_email = await request.app.mongodb["users"].find({'email': user.mail})
    #if existing_email is True:
    #    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST)
#    new_user = await request.app.mongodb['users'].insert_one(user)
#    created_user = await request.app.mongodb['users'].find_one({'_id': new_user.inserted_id})
#    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_user)


