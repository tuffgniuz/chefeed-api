

from http.client import HTTPException
from fastapi import APIRouter, Depends
from app.schemas.users import User
from app.auth.login_manager import current_active_user
from beanie.odm.fields import PydanticObjectId,WriteRules


router = APIRouter(prefix="/api/v1/users",tags=["Users"])

#get followers
#get followings


#post following
@router.post('/{id}/follow',response_description="Follow User")
async def follow_user(current_user = Depends(current_active_user)):
    print(current_user)
    """ user = await User.get(id)
    if user.id in current_user.following:
        return HTTPException(detail="You followed the user already")
    current_user.following.append(user)
    await current_user.save(link_rule=WriteRules.WRITE)
    user.followers.append(current_user)
    await user.save(link_rule=WriteRules.WRITE) """
    
    
    


    


