from fastapi import APIRouter, Depends
from models.user import User, UpdateUserDto
from controllers.user import UserController
from models.common import PaginationQueryDto
from config.database import get_db

router = APIRouter(prefix="/api/user", tags=["User"])


@router.get("/", summary="Fetch all users", response_model=list[User])
async def fetchAllUsers(query: PaginationQueryDto = Depends(), db=Depends(get_db)):
    return await UserController.fetchAllUsers(query, db)


@router.get("/{id}", summary="Fetch a user by id", response_model=User)
async def fetchUserById(id: str, db=Depends(get_db)):
    return await UserController.fetchUserById(id, db)


# update user by id
@router.put("/{id}", summary="Update a user by id")
async def updateUserById(id: str, user: UpdateUserDto, db=Depends(get_db)):
    return await UserController.updateUserById(id, user, db)
