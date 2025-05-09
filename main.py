from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# API tambahan untuk menampilkan semua item 
@app.get("/items")
def read_all_items():
    return {"items": ["item1", "item2", "item3"]}