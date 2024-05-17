from fastapi import APIRouter, Request, Path, Depends
import json
from typing import Annotated
from app.services.jwt_service import JWTService, User
from app.services.acl_service import GetAccessForUser

inventoryRouter = APIRouter(prefix="/inventory",)

@inventoryRouter.get("/")
async def read_items():
    f = open('./app/data/inventory/items.json')
    data = json.load(f)

    res = []

    for i in data:
        res.append(i)
    
    f.close()
    
    print(res)

    return {"inventory_items": res}

@inventoryRouter.get('/{sku}', dependencies=[Depends(GetAccessForUser("inventory.getBySku"))])
async def get_item(request: Request,  sku: str = Path(description="The SKU of the item you want to query")):
    f = open('./app/data/inventory/items.json')
    data = json.load(f)

    item = None

    for i in range(len(data)):
        if data[i]["sku"] == sku:
            item = data[i]
            break
    
    if not item:
        return {"error": "item not found"}
    
    return {"item": item}

