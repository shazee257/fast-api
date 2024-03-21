from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from controllers.auth import AuthController
from models.user import CreateUserDto
from config.database import get_db
from typing import Annotated
from models.user import User

router = APIRouter(prefix="/api/auth", tags=["Auth"])

db = Depends(get_db)


@router.post("/register", summary="Create a new user", response_model=User)
async def register(user: CreateUserDto, db=db):
    return await AuthController.register(user, db)


@router.post("/login", summary="Login user")
async def login(email: str, password: str, db=db):
    return await AuthController.login(email, password, db)


@router.get("/token", summary="Get token")
async def getToken(formData: Annotated[OAuth2PasswordRequestForm, Depends()], db=db):
    return await AuthController.getToken(formData.username, formData.password, db)
