from fastapi import APIRouter, HTTPException, Query
from models.user import User
from config.database import db
from schemas.user import serializeDict, serializeList
from bson import ObjectId
from utils.helpers import generateResponse

router = APIRouter()


@router.get("/", summary="Fetch all users")
async def fetchAllUsers(page: int = Query(1, ge=1), limit: int = Query(10, le=1000)):
    skip = (page - 1) * limit
    users = serializeList(db.user.find().skip(skip).limit(limit))
    return generateResponse("Users fetched successfully", users)


@router.post("/", summary="Create a new user")
async def createUser(user: User):
    result = db.user.insert_one(dict(user))
    user = serializeDict(db.user.find_one({"_id": result.inserted_id}))
    return generateResponse("User created successfully", user)


@router.get("/{id}", summary="Fetch a user by id")
async def fetchUser(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(422, "Invalid user ID format")

    user = serializeDict(db.user.find_one({"_id": ObjectId(id)}))
    if user:
        return generateResponse("User fetched successfully", user)
    raise HTTPException(404, "User not found")
