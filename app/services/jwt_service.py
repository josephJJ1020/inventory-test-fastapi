from jose import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from os import getenv
from datetime import timedelta, datetime, timezone
from typing import Annotated
from pydantic import BaseModel

ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer("/api/v1/auth/login")

class User(BaseModel):
    _id: str
    username: str
    role: str
    access: list[str]

class JWTService:
    @staticmethod
    def create_access_token(user: User):
        try:
            expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            user = {**user, "exp": expire}
            return jwt.encode(user, getenv("SECRET_KEY"))
        except Exception as e:
            print(e)
            return None
        
    
    @staticmethod
    def verify_token(token):
        try:
            return jwt.decode(token, getenv("SECRET_KEY"))
        except Exception as e:
            print(e)
            return None
    
    @staticmethod
    async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
        credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
        try:
            valid_user = JWTService.verify_token(token)

            if not valid_user:
                raise credentials_exception;
            return valid_user
        except Exception as e:
            print(e)
            raise credentials_exception
