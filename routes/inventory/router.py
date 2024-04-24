from fastapi import APIRouter, Path
import json

inventoryRouter = APIRouter(prefix="/inventory")

@inventoryRouter.get("/")
async def read_items():
    f = open('./data/inventory/items.json')
    data = json.load(f)

    res = []

    for i in data:
        res.append(i)
    
    f.close()
    
    print(res)

    return {"inventory_items": res}

@inventoryRouter.get('/{sku}')
async def get_item(sku: str = Path(description="The SKU of the item you want to query")):
    f = open('./data/inventory/items.json')
    data = json.load(f)

    item = None

    for i in range(len(data)):
        if data[i]["sku"] == sku:
            item = data[i]
            break
    
    if not item:
        return {"error": "item not found"}
    
    return {"item": item}