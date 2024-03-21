from fastapi import HTTPException
from bson import ObjectId
from config.database import db
from schemas.common import serializeDict, serializeList


class UserController:
    async def fetchUserById(id):
        if not ObjectId.is_valid(id):
            raise HTTPException(422, "Invalid user ID format")
        user = serializeDict(db.user.find_one({"_id": ObjectId(id)}))
        if user:
            return user
        raise HTTPException(404, "User not found")

    async def fetchAllUsers(query):
        skip = (query.page - 1) * query.limit
        users = serializeList(
            db.user.find(
                {
                    "$or": [
                        {"name": {"$regex": query.q, "$options": "i"}},
                        {"email": {"$regex": query.q, "$options": "i"}},
                    ]
                }
            )
            .skip(skip)
            .limit(query.limit)
        )
        return users

    async def createUser(user):
        result = db.user.insert_one(dict(user))
        user = serializeDict(db.user.find_one({"_id": result.inserted_id}))
        return user

    async def updateUserById(id, user):
        print("2nd user controller", user)
        if not ObjectId.is_valid(id):
            raise HTTPException(422, "Invalid user ID format")
        db.user.update_one({"_id": ObjectId(id)}, {"$set": dict(user)})
        return await UserController.fetchUserById(id)
