#import module
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

#create app
taskf1=FastAPI()

#product model
class Product(BaseModel):
    name:str
    price:float

#create list
products:List[Product]=[]

#post endpoint
@taskf1.post("/products",response_model=List[Product])
def add(product: Product):
    products.append(product)
    return products

#get endpoint
@taskf1.get("/products",response_model=List[Product])
def get():
    return products
