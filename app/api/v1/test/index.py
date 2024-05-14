from fastapi import APIRouter

testRouter = APIRouter(prefix='/test')

@testRouter.get("/")
def home():
    return "xdd"

@testRouter.get("/{param}")
def test(param):
    return {"Your data:" , param}