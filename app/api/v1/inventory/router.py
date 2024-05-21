from fastapi import APIRouter, Request, Path, Depends
import json
from pydantic import BaseModel, Field

from app.services.acl_service import GetAccessForUser
from app.repositories.inventory_repository import InventoryRepository

inventoryRouter = APIRouter(prefix="/inventory",)

class EditParams(BaseModel):
    name: str = Field(..., min_length="6")
    description: str = Field(..., min_length="10")
    cost: float = Field(..., gt=0)
    price: float = Field(..., gt=0)
    stocks: int = Field(..., gt=0)

@inventoryRouter.get("/")
async def read_items():
    f = open('./app/data/inventory/items.json')
    data = json.load(f)

    res = []

    for i in data:
        res.append(i)
    
    f.close()

    return {"inventory_items": res}

@inventoryRouter.get('/{id}', dependencies=[Depends(GetAccessForUser("inventory.getByID"))])
async def get_item(id: str = Path(description="The ID of the item you want to query")):    
    single_product = InventoryRepository.get_product_by_id(id)
    
    return single_product

@inventoryRouter.post('/{id}', dependencies=[Depends(GetAccessForUser("inventory.edit"))])
async def edit_by_id(editParams: EditParams, id: str = Path(description="The ID of the item you want to edit") ):
    name, description, cost, price, stocks = editParams.name, editParams.description, editParams.cost, editParams.price, editParams.stocks
    
    updated_product = InventoryRepository.update_by_id(id, name, description, cost, price, stocks)

    return updated_product