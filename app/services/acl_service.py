from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated

from app.services.jwt_service import JWTService
from app.repositories.user_repository import UserRepository

oauth2_scheme = OAuth2PasswordBearer("/api/v1/auth/login")

class GetAccessForUser:
    def __init__(self, access_name: str) -> None:
        self.access = access_name

    async def __call__(self, token: Annotated[str, Depends(oauth2_scheme)]):
        credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Unauthorized",
        headers={"WWW-Authenticate": "Bearer"},
    )
        user = None

        # get user from token
        decoded_user = JWTService.get_current_user(token)

        # get user from DB
        user_from_db = UserRepository.find_user_from_token(decoded_user["ID"], decoded_user["username"])

        if user_from_db and self.access in user_from_db["access"]:
            user = user_from_db

            return user
        else:
            raise credentials_exception
    
