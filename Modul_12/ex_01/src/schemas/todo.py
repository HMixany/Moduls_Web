from typing import Optional

from pydantic import BaseModel, EmailStr, Field


# class OwnerSchema(BaseModel):
#     fullname: str
#     email: EmailStr
#
#
# class OwnerResponse(OwnerSchema):
#     id: int = 1
#
#     class Config:
#         from_attributes = True


class TodoSchema(BaseModel):
    title: str = Field(min_length=3, max_length=50)
    description: str = Field(min_length=3, max_length=250)
    completed: Optional[bool] = False


class TodoUpdateSchema(TodoSchema):
    completed: bool


class TodoResponse(BaseModel):
    id: int = 1
    title: str
    description: str
    completed: bool

    class Config:
        from_attributes = True
