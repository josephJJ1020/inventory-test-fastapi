from starlette.requests import Request
from fastapi import Response
from fastapi.responses import JSONResponse
from typing import Callable
from os import getenv

from app.services.jwt_service import JWTService

async def getAccessToken(req: Request, call_next: Callable):
    accessToken = req.headers.get("accessToken")
    response: Response = await call_next(req)

    path = req.url.path.removeprefix("/api/v1/").split('/')[0]

    # disregard auth routes
    if (path == "auth"):
        return response

    if not accessToken or not JWTService.verify_token(accessToken):
         # get client IP
        
        return JSONResponse({"error": "Unauthorized"}, status_code=401)
    # error here
    return response
