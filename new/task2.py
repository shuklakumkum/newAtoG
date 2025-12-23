#import statement 
from fastapi import FastAPI
from pydantic import BaseModel

#To create API app
task2 = FastAPI()

#To create pydantic model
class User(BaseModel):
    name: str
    age: int
    email: str

#create user
@task2.post("/user")
def create(user: User):
    return {
        "message": "User is created", 
        "user": user   #return user data
    }

#To get API
@task2.get("/user/{user_id}")
def get_userid(user_id: int):  #user_id must be integer   
    return{
        "user_id":user_id  #return user_id
    }

#To get API
@task2.get("/search")
def search(keyword: str):
    return {
        "keyword":keyword  #return keyword value
    }