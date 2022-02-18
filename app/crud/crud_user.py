# from bson.objectid import ObjectId

from ..db.db import user_collection
from ..db.helpers import user_helper


async def retrieve_users():
    '''Returns all users from user_collection'''
    users = []

    async for user in user_collection.find():
        users.append(user_helper(user))

    return users


async def create_user(user_data) -> dict:
    '''Return new created user to user_collection'''
    user = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({'_id': user.inserted_id})

    return user_helper(new_user)
