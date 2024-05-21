from fastapi import APIRouter, Request, Path, Depends
import json
from typing import Annotated

from app.services.acl_service import GetAccessForUser
from app.repositories.inventory_repository import InventoryRepository

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

@inventoryRouter.get('/{id}', dependencies=[Depends(GetAccessForUser("inventory.getByID"))])
async def get_item(id: str = Path(description="The ID of the item you want to query")):    
    single_product = InventoryRepository.get_product_by_id(id)
    
    return single_product

