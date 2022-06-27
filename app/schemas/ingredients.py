from typing import Optional
from beanie.odm.documents import Document
from pydantic import Field


class Ingredient(Document):
    # id: str = Field(default_factory=uuid.uuid4, alias='_id')
    name : str = Field(...)
    # measurement : str = Field(...)
    # amount: int = Field(...)
    icon_url: Optional[str]
    
    class Settings:
        name = 'ingredients'

    class Config:
        # allow_population_by_field_name = True
        # arbitrary_types_allowed = True
        schema_extra = {
            'example':{
                'name' : 'Garlic',
                # 'measurement': 'PC',
                # 'amount':'2',
                'icon_url': 'str',
                }
            }

# class UpdateIngredientsSchema(BaseModel):
#     name = Optional[str]
#     measurement = Optional[str]
#     amount = Optional[int]
#     icon = Optional[str]

#     class Config:
#         arbitrary_types_allowed = True
#         json_encoders = {ObjectId: str}
#         schema_extra = {
#             'example':{
#                 'name' : 'Sugar',
#                 'measurement': 'str',
#                 'amount':'',
#                 'icon':'str',
#             }
#         }
