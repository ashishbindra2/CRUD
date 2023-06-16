from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# In-memory database
db: Dict[int, BaseModel] = {}


class Item(BaseModel):
    id: int
    name: str
    price: float


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    item = db.get(item_id)
    if item:
        return item
    else:
        return {"error": "Item not found"}


@app.post("/items")
async def create_item(item: Item):
    db[item.id] = item
    return item


@app.put("/items/{item_id}")
async def update_item(item_id: int, updated_item: Item):
    if item_id in db:
        db[item_id].name = updated_item.name
        db[item_id].price = updated_item.price
        return db[item_id]
    else:
        return {"error": "Item not found"}


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id in db:
        item = db.pop(item_id)
        return {"message": "Item deleted", "item": item}
    else:
        return {"error": "Item not found"}
