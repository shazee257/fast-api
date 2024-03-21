from fastapi import HTTPException, Depends
from schemas.common import serializeDict
from utils.helpers import hashPassword, verifyPassword
from config.database import get_db
from typing import Annotated

db = Annotated[get_db, Depends]

class AuthController:
    async def register(user, db):
        user.password = hashPassword(user.password)

        result = db.user.insert_one(dict(user))
        user = serializeDict(db.user.find_one({"_id": result.inserted_id}))
        return user

    async def login(email, password, db):
        user = serializeDict(db.user.find_one({"email": email}))
        if user:
            if verifyPassword(password, user.get("password")):
                return user
            raise HTTPException(401, "Invalid password")
        raise HTTPException(404, "User not found")
