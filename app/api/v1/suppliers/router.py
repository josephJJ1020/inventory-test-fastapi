from fastapi import APIRouter, Path
import json

supplierRouter = APIRouter(prefix="/suppliers")

@supplierRouter.get("/")
def get_suppliers():
    f = open("./app/data/suppliers/docs.json")
    data = json.load(f)

    f.close()

    return {"suppliers": data}

@supplierRouter.get('/{supplier_id}')
def get_single_supplier(supplier_id: str):
    f = open('./app/data/suppliers/docs.json')
    data = json.load(f)

    item = None

    for i in range(len(data)):
        if data[i]["_id"] == supplier_id:
            item = data[i]
            break;

    if not item:
        return {"error": "Supplier not found"}

    return {"supplier": item}

