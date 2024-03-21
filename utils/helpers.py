from passlib.context import CryptContext
from datetime import datetime
from jose import jwt
import os

pwd_context = CryptContext(schemes=["sha256_crypt", "des_crypt"])


def hashPassword(password):
    return pwd_context.hash(password)


def verifyPassword(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def createAccessToken(name: str, email: str, id: str, expiresDelta: int = 30):
    encode = {"id": id, "name": name, "email": email}
    expires = datetime.utcnow() + expiresDelta
    encode.update({"exp": expires})
    return jwt.encode(
        encode, os.environ.get("SECRET_KEY"), algorithm=os.environ.get("ALGORITHM")
    )
