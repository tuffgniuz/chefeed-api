from pydantic import BaseModel, EmailStr, Field

# TODO: add password


class UserSchema(BaseModel):
    """
    Schema for User object 

    Attributes
    ----------
    firstname: str
        firstname of the user
    lastname: str
        lastname of the user
    email: EmailStr
        email of user (used to authenticate)
    """
    firstname: str = Field(...)
    lastname: str = Field(...)
    email: EmailStr = Field(...)

    class Config:
        schema_extra = {
            'example': {
                'firstname': 'Jane',
                'lastname': 'Doe',
                'email': 'john@doe.com'
            }
        }


def ResponseModel(data, message):
    return {
        'data': [data],
        'code': 200,
        'message': message
    }


def ErrorResponseModel(error, code, message):
    return {
        'error': error, 'code': code, 'message': message
    }
