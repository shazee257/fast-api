from pydantic import BaseModel, Field, validator, EmailStr, constr, Extra
from typing import Optional


class User(BaseModel):
    id: Optional[str] = Field(None, alias="_id", exclude_unset=False)
    name: str
    email: EmailStr
    password: str


class CreateUserDto(BaseModel):
    name: str
    email: EmailStr
    password: str


class UpdateUserDto(BaseModel):
    name: str
    email: EmailStr
