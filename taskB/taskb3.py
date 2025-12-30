#import module
from fastapi import FastAPI

#create app
taskb3=FastAPI()

#product list
products=[
    {"name":"Laptop","price":50000},
    {"name":"Mouse","price":500},
    {"name":"Keyboard","price":1500},
    {"name":"Monitor","price":15000}
]

#get endpoint
@taskb3.get("/products/filter")
def filter(min_price:int):
    result=[]
    for product in products:
        if product["price"]>=min_price:
            result.append(product)

    #return rsult
    return result