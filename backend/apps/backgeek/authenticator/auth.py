from typing import Union

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
import os
from pydantic import BaseModel
from passlib.context import CryptContext


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class User(BaseModel):
    username: str
    email: Union[str, None] = None
    disabled: Union[bool, None] = None
    uuid: str


class UserInDB(User):
    hashed_pass: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

print(os.environ['SECRET_KEY'])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def oath_keeper(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):



