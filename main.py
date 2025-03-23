# windows + r, cmd
# cd c:\Users\Ian\meu_projeto_fastapi
# python -m venv venv
# venv\Scripts\activate
# uvicorn main:app --reload


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"} 
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price}
