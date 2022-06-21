from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from app.schemas.user import UserCreate, UserRead

from .api.api_v1.endpoints.user import router as UserRouter
from .api.api_v1.endpoints.recipe import router as RecipeRouter
from .api.api_v1.endpoints.User.register import router as UserRegisterRouter
from .api.api_v1.endpoints.User.user_auth import router as AuthenticationRouter
#from fastapi_users.router import get_register_router
#from .api.api_v1.endpoints.User.user_register import chefeed_users,authentication
#from .api.api_v1.endpoints.category import router as CategoryRouter
#from .api.api_v1.endpoints.ingredients import router as IngredientRouter
#from .api.api_v1.endpoints.bookmark
#  import router as BookmarksRouter
from .config import settings

app = FastAPI()

#chefeed_users = FastAPIUsers()

# TODO: add docstrings


@app.on_event('startup')
async def startup_db_client():
    app.mongo_client = AsyncIOMotorClient(settings.DB_URL)
    app.mongodb = app.mongo_client.chefeed_db


@app.on_event('shutdown')
async def shutdown_db_client():
    app.mongo_client.close()


app.include_router(UserRouter)
app.include_router(RecipeRouter)
app.include_router(UserRegisterRouter)
app.include_router(AuthenticationRouter)


#Testing Fastapi-User BUt Failed coz yikes

#app.include_router(chefeed_users.get_register_router(UserRead,UserCreate),prefix="/auth",tags=["auth"])
#app.include_router(chefeed_users.get_auth_router(authentication),prefix="/auth/jwt",tags=["auth"])
#app.include_router(chefeed_users.get_reset_password_router)
#password reset router??


