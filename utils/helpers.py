from passlib.context import CryptContext
from datetime import datetime
from jose import jwt


SECRET_KEY = "nCXEmL3K2hVkbS7uqtTFe4v8dfyQjNJ9WawHZxMBc6GrRgsPAD"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["sha256_crypt", "des_crypt"])


def hashPassword(password):
    return pwd_context.hash(password)


def verifyPassword(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def createAccessToken(name: str, email: str, id: str, expiresDelta: int = 30):
    encode = {"id": id, "name": name, "email": email}
    expires = datetime.utcnow() + expiresDelta
    encode.update({"exp": expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
