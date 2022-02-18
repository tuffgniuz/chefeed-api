from ..schemas.user import UserSchema


def user_helper(user: UserSchema) -> dict:
    return {
        'id': str(user['_id']),
        'firstname': user['firstname'],
        'lastname': user['lastname'],
        'email': user['email']
    }
