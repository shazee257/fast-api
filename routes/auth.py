from fastapi import APIRouter
from controllers.auth import AuthController
from models.user import CreateUserDto

router = APIRouter(prefix="/api/auth", tags=["Auth"])


@router.post("/register", summary="Create a new user")
async def register(user: CreateUserDto):
    return await AuthController.register(user)


@router.post("/login", summary="Login user")
async def login(email: str, password: str):
    return await AuthController.login(email, password)
