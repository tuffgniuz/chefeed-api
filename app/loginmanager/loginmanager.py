from typing import List, Optional
from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Body
from starlette.requests import Request
from starlette.responses import JSONResponse
from ..schemas.user import TokenData, UserSchema
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from ..config.settings import py_db
from datetime import timedelta,datetime

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

#For Hasing Passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "f5f1a7ff0fe314bdfc6a203c5df007903119d65a09609f9a2624c420dfa0920e"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 20

#For Verify Passwords
def verify_password(user_password,hashed_password):
    return pwd_context.verify(user_password,hashed_password)

#To Get Hashed Password
def get_hash_password(user_password):
    return pwd_context.hash(user_password)

#To get User
def get_user(username:str):

    result_from_query = py_db["users"].find({'username':username},{'_id':False}) 
    final_result = list(result_from_query)

    if len(final_result) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="USERNAME NOT FOUND")
    if len(final_result) > 1:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="MULTIPLE USERNAME FOUND")
    
    user_dict = final_result[0]

    class Response:
        def __init__(self,username,email,hash_password):
            self.username = username
            self.email = email
            self.hash_password = hash_password
        
        response = Response(
            user_dict['username'],
            user_dict['email'],
            user_dict['hash_password']
        )
    return response


def authenticate_user(username:str,password:str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password,user.hash_password):
        return False
    return user

def create_access_token(data:dict, expires_delta: Optional[timedelta]=None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=20)
    to_encode.update({'exp':expire})
    
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credential Validation Failed",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("_id")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: UserSchema = Depends(get_current_user)):
    return current_user


