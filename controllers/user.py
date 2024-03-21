from fastapi import HTTPException, Depends
from bson import ObjectId
from schemas.common import serializeDict, serializeList
from config.database import get_db


class UserController:
    async def fetchUserById(id, db):
        if not ObjectId.is_valid(id):
            raise HTTPException(422, "Invalid user ID format")
        user = serializeDict(db.user.find_one({"_id": ObjectId(id)}))
        if user:
            return user
        raise HTTPException(404, "User not found")

    async def fetchAllUsers(query, db):
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

    async def updateUserById(id, user, db):
        print("2nd user controller", user)
        if not ObjectId.is_valid(id):
            raise HTTPException(422, "Invalid user ID format")
        db.user.update_one({"_id": ObjectId(id)}, {"$set": dict(user)})
        return await UserController.fetchUserById(id, db)
