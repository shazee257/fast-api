from fastapi import APIRouter, Depends
from models.user import User, CreateUserDto, UpdateUserDto
from controllers.user import UserController
from models.common import PaginationQueryDto

router = APIRouter()


@router.get("/", summary="Fetch all users", response_model=list[User])
async def fetchAllUsers(query: PaginationQueryDto = Depends()):
    return await UserController.fetchAllUsers(query)


@router.get("/{id}", summary="Fetch a user by id", response_model=User)
async def fetchUserById(id: str):
    return await UserController.fetchUserById(id)


@router.post("/", summary="Create a new user")
async def createUser(user: CreateUserDto):
    return await UserController.createUser(user)


# update user by id
@router.put("/{id}", summary="Update a user by id")
async def updateUserById(id: str, user: UpdateUserDto):
    return await UserController.updateUserById(id, user)
