from http.client import HTTPException
from fastapi import APIRouter, Depends
from app.schemas.users import User,UserUpdate
from app.auth.login_manager import current_active_user
from beanie.odm.fields import PydanticObjectId,WriteRules
from starlette.responses import JSONResponse

#


router = APIRouter(prefix="/api/v1/users",tags=["Users"])

#show user profile (get user by ID)
@router.get("/{id}", response_description="Get User Data")
async def get_user(id:PydanticObjectId) -> User:
    user = await User.find_one(User.id==id,fetch_links=True)
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return user


@router.put('/{id}',response_description="Update User Profile")
async def update_user(id:PydanticObjectId,request:UserUpdate, current_user = Depends(current_active_user)) -> User:
    request = {k: v for k, v in request.dict().items() if v is not None}
    update_query = {"$set": {
        field: value for field, value in request.items()
    }}

    user_profile = await current_user.get(id)
    if not user_profile:
        raise HTTPException(
            status_code=404,
            detail="User not found!"
        )

    await user_profile.update(update_query)
    return user_profile

#get followers
#get followings


#post following
@router.post('/{id}/follow',response_description="Follow User")
async def follow_user(followed_user_id: PydanticObjectId, current_user = Depends(current_active_user)):
    user = await User.get(followed_user_id)
    if user.id not in current_user.following:
        current_user.following.append(user)
        await current_user.save(link_rule=WriteRules.WRITE)
        cu = await User.get(current_user.id)
        user.followers.append(cu)
        await user.save(link_rule=WriteRules.WRITE) 

    return JSONResponse(detail="You followed the user already")
    #
    
    
    


    


