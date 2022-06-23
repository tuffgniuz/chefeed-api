from fastapi import APIRouter, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Body
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.schemas.user import UserSchema
from ....loginmanager.loginmanager import get_current_active_user

from ....schemas.user import UserSchema
from ....schemas.bookmarks import BookmarksSchema

router = APIRouter(prefix='/api/v1/bookmarks',tags=['Bookmarks'])

"""RETRIEVE ALL BOOKMARKS"""
@router.get('/',response_description='List all bookmarks' ,response_model=list[BookmarksSchema],)
async def retrieve_bookmarks(request:Request, current_user: UserSchema = Depends(get_current_active_user)):
    bookmarks = await request.app.mongodb['bookmarks'].find().to_list(1000)
    return bookmarks

"""RETRIEVE BY ID"""
@router.get("/{id}",response_description="Get bookmark by id")
async def retrieve_bookmark_by_id(id: str,request: Request):
    bookmark = await request.app.mongodb["bookmarks"].find_one({"_id":id})
    if bookmark is not None:
        return bookmark
    raise HTTPException(status_code=400, detail=f"Bookmark with {id} is not found")

"""CREATE NEW BOOKMARK"""
@router.post('/',response_description='Add new Bookmark', response_model=BookmarksSchema)
async def create_bookmark(request:Request,bookmark:BookmarksSchema = Body(...)):
    bookmark = jsonable_encoder(bookmark)
    new_bookmark = await request.app.mongodb['bookmarks'].insert_one(bookmark)
    created_bookmark = await request.app.mongodb['bookmarks'].find_one({'_id':new_bookmark.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_bookmark)

"""DELETE BOOKMARK BY ID"""
@router.delete("/{id}", response_description="Delete Bookmark")
async def delete_bookmark(id:str, request:Request):
    delete_bookmark = await request.app.mongodb["bookmarks"].delete_one({"_id": id})
    if delete_bookmark.deleted_count == 1:
        return "Bookmarks has been successfully deleted"
    raise HTTPException(status_code=404,detail=f"Bookmark with {id} is not found")


