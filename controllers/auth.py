from fastapi import HTTPException,Depends
from schemas.common import serializeDict
from utils.helpers import hashPassword, verifyPassword, createAccessToken
from datetime import timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated


oauth2Bearer = OAuth2PasswordBearer(tokenUrl="/api/auth/token")


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

    # async def getToken(username, password, db):
    async def getToken(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db):
        user = authenticateUser(form_data.username, form_data.password, db)
        if not user:
            raise HTTPException(401, "Invalid credentials")
        if not verifyPassword(password, user.get("password")):
            raise HTTPException(401, "Invalid credentials")
        
        accessToken = await AuthController.createAccessToken(
            user.get("name"),
            user.get("email"),
            str(user.get("_id")),
            timedelta(minutes=20),
        )
        return {"user": user, "accessToken": accessToken}

        



    def authenticateUser(username, password, db):
        user = serializeDict(db.user.find_one({"name": username}))
        return user
        
        


        # user = serializeDict(db.user.find_one({"name": username}))
        # if not user:
        #     raise HTTPException(401, "Invalid credentials")
        # if not verifyPassword(password, user.get("password")):
        #     raise HTTPException(401, "Invalid credentials")

        # accessToken = await AuthController.createAccessToken(
        #     user.get("name"),
        #     user.get("email"),
        #     str(user.get("_id")),
        #     timedelta(minutes=20),
        # )
