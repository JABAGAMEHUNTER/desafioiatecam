from typing import Annotated
from typing import Union
from datetime import date
from enum import Enum


from fastapi import FastAPI, Query
from pydantic import BaseModel

#import modules
import database


app = FastAPI()

@app.get("/")
def index():
    return {"data": "foo"}

@app.get("/login/{user_id}")
async def login(userid: Annotated[str, Query(min_length=8)]):
    results = {"userid": [{"user_id":"userid"}, {"password": "password123"}]}
    if userid:
        results.update({"userid": userid})
    return results

@app.get("/logout/{user_id}")
def logout(user_id: int):
    return {"item_id": user_id}

@app.post("/item/register/{item_id}")
async def register_item(item: Annotated[list[str], Query()] = ["item_name", "item_category"]):
    query_items = {"item": item}
    return query_items

@app.put("/item/update/{item_id}")
async def update_item(
    item: Annotated[str | None, Query(title="name", min_length=8)] = None
):
    results = {"items": [{"title": "name"}, {"description": "description"}]}
    if item:
        results.update({"item": item})
    return results

@app.delete("/item/delete/{item_id}")
async def delete_item():
    return {"item_id": item_id, "status":"deletado"} 

@app.post("/category/register/{category_id}")
async def register_category(category: Annotated[list[str], Query()] = ["category", "description"]):
    category = {"category": category}
    return category 

@app.put("/category/update/{item_id}")
async def update_category(
    category: Annotated[str | None, Query(title="name", min_length=8)] = None
):
    results = {"category": [{"title": "name"}, {"description": "description"}]}
    if category:
        results.update({"category": category})
    return results

@app.delete("/category/delete/{category_id}")
async def delete_category():
    return {"category_id": category_id, "status":"deletada"} 
