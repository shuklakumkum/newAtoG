#import module
from fastapi import FastAPI

#create app
taskA=FastAPI()

#product data
products=[
    {"name":"Laptop","price":50000},
    {"name":"Mouse","price":500},
    {"name":"keyboard","price":1500}
]

#get endpoint
@taskA.get("/products/highest")
def get():
    high_product=products[0]
    for product in products:
        if product["price"]>high_product["price"]:
            high_product=product

    return high_product
                                         