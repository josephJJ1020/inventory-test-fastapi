from fastapi import APIRouter, Depends
from typing import Annotated
from pydantic import BaseModel
from os import getenv
from fastapi.responses import JSONResponse

from app.repositories.user_repository import UserRepository
from app.services.jwt_service import JWTService, User
from app.services.acl_service import GetAccessForUser

class LoginParams(BaseModel):
    username: str
    password: str

authRouter = APIRouter(prefix="/auth")

@authRouter.post("/login/")
async def login(user: LoginParams):
    """
    Accepts JSON request body
    """
    username, password = user.username, user.password

    valid_user = UserRepository.find_user(username, password)

    if not valid_user:
        return JSONResponse({"error": "User not found", "status": 0}, 400)


    access_token = JWTService.create_access_token({"username": valid_user["username"], "ID": valid_user["ID"], "role_id": valid_user["role_id"]})

    return {"accessToken": access_token}

@authRouter.get('/me')
async def get_me(current_user: Annotated[User, Depends(GetAccessForUser("auth.me"))]):
    return current_user