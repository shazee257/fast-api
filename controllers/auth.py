from fastapi import HTTPException
from schemas.common import serializeDict
from utils.helpers import hashPassword, verifyPassword, createAccessToken
from datetime import timedelta


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
                accessToken = createAccessToken(
                    user.get("name"),
                    user.get("email"),
                    str(user.get("_id")),
                    timedelta(minutes=20),
                )

                return {"user": user, "accessToken": accessToken}
            raise HTTPException(401, "Invalid password")
        raise HTTPException(404, "User not found")
