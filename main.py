from fastapi import FastAPI, Request, Response
from typing import Callable
from dotenv import load_dotenv

# import API routes
from app.api.v1.test.index import testRouter
from app.api.v1.inventory.router import inventoryRouter
from app.api.v1.suppliers.router import supplierRouter
from app.api.v1.auth.router import authRouter


from app.middleware.getAccessToken import getAccessToken

# init FastAPI
app = FastAPI()

load_dotenv()

# import routers
app.include_router(authRouter, prefix="/api/v1")
app.include_router(testRouter)
app.include_router(inventoryRouter, prefix="/api/v1")
app.include_router(supplierRouter, prefix="/api/v1")

@app.middleware("http")
async def getAccessTokenMiddleware(request: Request, call_next: Callable):
    return await getAccessToken(request, call_next)

@app.get("/")
def home():
    data = {"data": "Hello World"}
    return data

