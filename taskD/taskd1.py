#impoer module
from fastapi import FastAPI

#create app 
taskd1=FastAPI()

#product list
products=[
    {"name":"Laptop","category":"Electronics"},
    {"name":"Mouse","category":"Electronics"},
    {"name":"Shirt","category":"Clothing"}
]

#get endpoint
@taskd1.get("/products/search")
def search(keyword: str=""):
    if keyword=="":
        return products
    result=[]

    #loop
    for product in products:
        if keyword.lower() in product["name"].lower():
            result.append(product)

    #return result
    return result