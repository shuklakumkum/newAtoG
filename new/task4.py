#import librarie
from fastapi import FastAPI, HTTPException,status
from pydantic import BaseModel
from typing import List

#create app
task4 = FastAPI()

#user model
class User(BaseModel):
    name:str
    age:int
    email:str

#fake database
users=[]

#create user in list
@task4.post("/user",status_code=201)
def create_user(user:User):
   users.append(user)  
   return{
        "message":"user is created successfully", 
        "user":user
    }

#get user from list
@task4.get("/user",status_code=200)  
def get():
    return users
    
#update user in list
@task4.put("/user/{user_id}",status_code=200) 
def update(user_id: int, user:User):
    if user_id<0 or user_id>=len(users):
        raise HTTPException(
            status_code=404,
            detail="user is not found"
        )
    users[user_id]=user    
    return{                 
        "message":"user is updated successfully",
        "user":user
        }

#delete user from list
@task4.delete("/user/{user_id}", status_code=200)
def delete(user_id: int):
    if user_id<0 or user_id>=len(users):
        raise HTTPException(
            status_code=404,
            detail="user is not found"
        )

    deleted_user=users.pop(user_id)
    return {                      
        "message": "user is deleted successfully",
        "user": deleted_user
    }


