from fastapi import FastAPI, Request, Response
from typing import Callable
from dotenv import load_dotenv

# import API routes
from app.api.v1.test.index import testRouter
from app.api.v1.inventory.router import inventoryRouter
from app.api.v1.suppliers.router import supplierRouter


from app.middleware.getAccessToken import getAccessToken

# init FastAPI
app = FastAPI()

load_dotenv()

# import routers
app.include_router(testRouter)
app.include_router(inventoryRouter)
app.include_router(supplierRouter)

@app.get("/")
def home():
    data = {"data": "Hello World"}
    return data

@app.middleware("http")
async def getAccessTokenMiddleware(request: Request, call_next: Callable):
    return await getAccessToken(request, call_next)