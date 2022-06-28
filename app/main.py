from fastapi import FastAPI
from beanie import init_beanie

from app.db import db
from app.schemas.category import Category
from app.schemas.ingredients import Ingredient
from app.schemas.recipe import Recipe
from app.schemas.users import User, UserCreate, UserRead
from app.schemas.review import Review
from app.auth.auth_backend import auth_backend
from app.auth.login_manager import fastapi_users, current_active_user
# from motor.motor_asyncio import AsyncIOMotorClient


from .api.api_v1.endpoints.recipe import router as RecipeRouter
from .api.api_v1.endpoints.category import router as CategoryRouter
from .api.api_v1.endpoints.ingredients import router as IngredientRouter
from .api.api_v1.endpoints.review import router as ReviewRouter
from .api.api_v1.endpoints.users import router as UserRouter

# #from .api.api_v1.endpoints.bookmark import router as BookmarksRouter
# #from .api.api_v1.endpoints.User.register import router as UserRegisterRouter
# from .api.api_v1.endpoints.User.user_auth import router as AuthenticationRouter
# from .api.api_v1.endpoints.bookmark import router as BookmarkRouter
# # from .api.api_v1.endpoints.review import review as ReviewRouter
#
# from .config import settings

app = FastAPI()

app.include_router(RecipeRouter)
app.include_router(CategoryRouter)
app.include_router(IngredientRouter)
app.include_router(ReviewRouter)
app.include_router(UserRouter)

app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix='/auth', tags=['auth']
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['auth']
)


@app.on_event('startup')
async def on_startup():
    await init_beanie(
        database=db,
        document_models=[User, Recipe, Ingredient, Category, Review]
    )

# @app.on_event('startup')
# async def startup_db_client():
#     app.mongo_client = AsyncIOMotorClient(settings.DB_URL)
#     app.mongodb = app.mongo_client.chefeed_db


# @app.on_event('shutdown')
# async def shutdown_db_client():
#     app.mongo_client.close()


# app.include_router(RecipeRouter)
# app.include_router(CategoryRouter)
# app.include_router(IngredientRouter)
# app.include_router(BookmarkRouter)


# Testing Fastapi-User BUt Failed coz yikes
