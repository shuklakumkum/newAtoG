#import module
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

#create app
taskg=FastAPI()

#input model
class User(BaseModel):
    name:str
    email:str
    password:str

#response model
class UserResponse(BaseModel):
    name:str
    email:str

#user list
users:List[User]=[]

#create user
@taskg.post("/users",response_model=UserResponse)
def create(user:User):
    users.append(user)
    return user

#get user
@taskg.get("/users",response_model=List[UserResponse])
def get():
    return users