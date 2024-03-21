from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["sha256_crypt", "des_crypt"])


def hashPassword(password):
    return pwd_context.hash(password)


def verifyPassword(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
