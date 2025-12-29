#import module
from fastapi import FastAPI
from pydantic import BaseModel,Field

#create app
taskf2=FastAPI()

#product model
class Product(BaseModel):
    name:str=Field(min_length=3,max_length=50)
    price:float=Field(gt=0)
    decription:str=Field(default="no description")

#create list
produts=[]

#post endpoint
@taskf2.post("/products")
def add(product:Product):
    produts.append(product)
    return{"message":"product add successfully","product":Product}
