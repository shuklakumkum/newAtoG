#import module
from fastapi import FastAPI

#create app
task = FastAPI()

#product data
products=[
    {"id":1,"name":"Laptop","price":50000},
    {"id":2,"name":"Mouse","price":500}
]

#get endpoint
@task.get("/product/check/{p_name}")
def check(p_name:str):
    for product in products:
       if product["name"] ==p_name:
        return{
             "success":True,
             "message":"product is found"
    }

#return message
    return {
        "success": False,
        "message":"product is not found"
    }
