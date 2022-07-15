from fastapi import APIRouter, Depends, HTTPException
from app.schemas.users import User, UserUpdate
from app.auth.login_manager import current_active_user
from beanie.odm.fields import PydanticObjectId, WriteRules
from starlette.responses import JSONResponse


router = APIRouter(prefix="/api/v1/users", tags=["Users"])


@router.post('/follow/{user_id}', response_description="Follow User")
async def follow_user(user_id: PydanticObjectId, current_user: User = Depends(current_active_user)):
    user = await User.find_one(User.id == user_id)

    current_user.following.append(user)

    await current_user.save(link_rule=WriteRules.WRITE)

    try:
        user.followers.append(current_user)

        await user.save(link_rule=WriteRules.WRITE)
    except Exception:
        print(user)
