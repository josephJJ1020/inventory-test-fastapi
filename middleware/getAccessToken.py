from starlette.requests import Request
from fastapi import Response
from fastapi.responses import JSONResponse
from typing import Callable

from os import getenv


async def getAccessToken(req: Request, call_next: Callable):
    accessToken = req.headers.get("accessToken")

    response: Response = await call_next(req)

    if not accessToken or accessToken != getenv("ACCESS_TOKEN"):
         # get client IP
        ip = req.client.host
        print("no access token found@", ip)
        
        return JSONResponse({"error": "Unauthorized"}, status_code=405)
    # error here
    return response
