from pydantic import BaseModel, EmailStr, Field


class HomeSchema(BaseModel):
    name = str
    level = int
    gold = int
    tree = int
    stone = int
    corn = int
    iron = int
    crystals = str


class HomeResponse(HomeSchema):
    id: int = 1

    class Config:
        from_attributes = True


class PorterSchema(BaseModel):
    level = int
    gold = int
    tree = int
    stone = int
    corn = int
    iron = int
    crystals = str


class PorterResponse(PorterSchema):
    id: int = 1

    class Config:
        from_attributes = True
