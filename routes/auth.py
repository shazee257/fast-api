from fastapi import APIRouter, Depends
from controllers.auth import AuthController
from models.user import CreateUserDto
from config.database import get_db

router = APIRouter(prefix="/api/auth", tags=["Auth"])

db = Depends(get_db)


@router.post("/register", summary="Create a new user")
async def register(user: CreateUserDto, db=db):
    return await AuthController.register(user, db)


@router.post("/login", summary="Login user")
async def login(email: str, password: str, db=db):
    return await AuthController.login(email, password, db)
