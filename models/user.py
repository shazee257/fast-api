from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class User(BaseModel):
    id: Optional[str] = Field(None, alias="_id", exclude_unset=False)
    name: str
    email: str
    password: str


class CreateUserDto(BaseModel):
    name: str
    email: EmailStr
    password: str


class UpdateUserDto(BaseModel):
    name: str
    email: EmailStr
