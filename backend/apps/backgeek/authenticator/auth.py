from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

async def oath_keeper(token: str = Depends(oauth2_scheme)):
    return token
