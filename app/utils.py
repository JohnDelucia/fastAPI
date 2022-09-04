from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") #using bcrypt as password hashing algorithm

def hash(password: str):
    return pwd_context.hash(password)

#verify user entered password equals hashed password stored
def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
