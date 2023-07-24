from typing import Union
from datetime import date
from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.get("/name/{first_name},{last_name}")
async def read_item(first_name, last_name):
    def get_full_name(first_name, last_name):
        full_name = first_name.title() + " " + last_name.title()
        return {"full_name": full_name}
        print(get_full_name("john", "doe"))


@app.get("/name/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

#Enum
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    letnet = "letnet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "letnet":
        return {"mode_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

#Path convertor
@app.get("/fies/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

#Query parameters
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

#Query parameters with if
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
                {"description": "This is an amazing item that has a long description"}
                 )
    return item
        #return {"item_id": item_id, "q": q}
    #return {"item_id": item_id}

#Query parameter type conversion


#Multiple query items
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
                {"description": "This is an amazing item that has long description"}
        )
    return item


#Declare a variable as str
#and get editor support inside the function
def main(user_id: str):
    return user_id
    name: str
    joined: date

class User(BaseModel):
    id: int
    name: str
    joined: date

my_user: User = User(id=3, name="John DOe", joined="2018-07-19")

second_user_data = {
    "id": 4,
    "name": "Mary",
    "joined": "2018-11-30",
}

my_second_user: User = User(**second_user_data)

