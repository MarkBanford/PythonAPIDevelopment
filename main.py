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


