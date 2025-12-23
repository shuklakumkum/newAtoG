#import module
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import requests

#create app
task5 = FastAPI(title="Error handling")

#user module
class User(BaseModel):
    name:str
    age:int
    email:str

#fake database
users=[]

#create new user in database
@task5.post("/users")
def create_user(user:User):
    for u in users:
        if u.email == user.email:
            raise HTTPException(status_code=400,detail="user is already exists")
        
#To add user in database
    users.append(user)
    return {
        "message":"user is created successfully",
        "user":users
}

#return all user from database
@task5.get("/users")
def get():
    return users

#fetch task 
@task5.get("/task")
def get():
    try :
         response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
         if response.status_code !=200:
            raise HTTPException(status_code=502,detail="failed to get the task")
         return response.json()
    except requests.RequestException:
        raise HTTPException(status_code=502,detail="API request is failed")



