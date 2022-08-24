from typing import Union
import requests
from fastapi import FastAPI
from pydantic import BaseModel # adicionar en los imports en el main.py

class Item(BaseModel):
    name: str
    price: str
    is_offer: Union[bool, None] = None

        
app = FastAPI()


@app.get("/")
def read_root():
    url = "https://6303e4b50de3cd918b3fd56c.mockapi.io/items"
    response = requests.get(url,{}, timeout = 5)
    return {"items": response.json()}


@app.get("/item/{item_id}")
def read_item(item_id: int):
    url = "https://6303e4b50de3cd918b3fd56c.mockapi.io/items"
    response = requests.get(url,{}, timeout = 5)
    return {"items": response.json()[item_id-1]}


@app.put("/items/{item_id}")
def update_item(item_id:int,item:Item):
    headers = {'Content-type': 'application/json', 'Accept': 'Application/json'}
    url = "https://6303e4b50de3cd918b3fd56c.mockapi.io/items"
    requests.put(url+"/"+str(item_id), item.json(), headers=headers)
    return "Exitoso"

@app.post("/items/")
def create_item(item:Item):
    url = "https://6303e4b50de3cd918b3fd56c.mockapi.io/items"
    requests.post(url, item.json())
    return "Exitoso"

@app.delete("/items/{item_id}")
def delet_item(item_id):
    url = "https://6303e4b50de3cd918b3fd56c.mockapi.io/items"
    response = requests.delete(url+"/"+str(item_id), timeout=5)
    return "Exitoso"
