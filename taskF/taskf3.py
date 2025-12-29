#import module
from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel

#create app
taskf3=FastAPI()

#Item modle
class Item(BaseModel):
    name:str

#create list
items=[]

#create new item
@taskf3.post("/items",status_code=status.HTTP_201_CREATED)
def create(item:Item):
    items.append(item)
    return item

#get item
@taskf3.get("/items/{item_id}")
def get(item_id:int):
    if item_id<0 or item_id>=len(items):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="item is not found")
    return items[item_id]

#delete item
@taskf3.get("/items/{item_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete(item_id:int):
    if item_id<0 or item_id>=len(items):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="item is not found")
    items.pop(item_id)
    return
