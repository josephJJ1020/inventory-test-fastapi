from fastapi import FastAPI, Request, Response
from typing import Callable
import time
from dotenv import load_dotenv

from routes.test.index import testRouter
from routes.inventory.router import inventoryRouter
from routes.suppliers.router import supplierRouter

from middleware.getAccessToken import getAccessToken

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