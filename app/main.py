from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from beanie import init_beanie

from app.db import db
from app.schemas.category import Category
from app.schemas.ingredients import Ingredient
from app.schemas.recipe import Recipe
from app.schemas.review import Review
from app.schemas.users import User, UserCreate, UserRead, UserUpdate
from app.schemas.review import Review
from app.auth.auth_backend import auth_backend
from app.auth.login_manager import fastapi_users


from .api.api_v1.endpoints.recipe import router as RecipeRouter
from .api.api_v1.endpoints.category import router as CategoryRouter
from .api.api_v1.endpoints.ingredients import router as IngredientRouter
from .api.api_v1.endpoints.review import router as ReviewRouter
from .api.api_v1.endpoints.users import router as UserRouter

app = FastAPI()

origins = [
    "http://10.15.136.17:19000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix='/auth', tags=['auth']
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['auth']
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix='/users',
    tags=['/users']
)
app.include_router(RecipeRouter)
app.include_router(CategoryRouter)
app.include_router(IngredientRouter)
app.include_router(ReviewRouter)
# app.include_router(UserRouter)


@app.on_event('startup')
async def on_startup():
    await init_beanie(
        database=db,
        document_models=[User, Recipe, Ingredient, Category, Review]
    )
