from fastapi import FastAPI

from .api.api_v1.endpoints.user import router as UserRouter

app = FastAPI()

app.include_router(UserRouter)


@app.get('/')
async def index():
    return {'msg': 'Wow'}
