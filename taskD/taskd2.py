#import module
from fastapi import FastAPI

#create app
taskd2=FastAPI()

#list item
items=[1,2,3,4,5,6,7,8,9,10]

#get API
@taskd2.get("/items")
def get(page:int=1,per_page:int=5):
    start=(page-1)*per_page  #it calculate start index
    end=start+per_page       #it calculate end index
    
    #return item
    return items[start:end]
