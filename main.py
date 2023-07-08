'''uvicorn main:app --reload
POSTMAN app for testing
Below is an inventory management system
'''
from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Category(Enum):
    TOOLS = "tools"
    CONSUMABLES = "consumables"


class Item(BaseModel):
    name: str
    price: float
    count: int
    id: int
    category: Category


items = {
    0: Item(name="Hammer", price=9.99, count=20, id=0, category=Category.TOOLS),
    1: Item(name="Nails", price=1.99, count=100, id=2, category=Category.CONSUMABLES)

}


# we can use Pydantic types such as dict[int,Item]
@app.get("/")
def index() -> dict[str, dict[int, Item]]:
    return {"items": items}
