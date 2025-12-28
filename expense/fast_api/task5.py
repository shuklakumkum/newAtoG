from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel,Field,validator
import requests


task5=FastAPI(title="error handling")

class User(BaseModel):
    name:str
    age:int
    email:str

users=[]

@task5.post("/users")
def create_user(user:User):
    for user in users:
        if user.email == users.email:
            raise HTTPException(status_code=400,detail="user is already exists in database")
        
        users.append(user)
        return{"message":"user is created successfully","user":user}
    
    @task5.get("/users")
    def get_users():
        return{"user": users}
    
    @task5.get("/task")
    def get_task():
        try:
          response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
          if response.status_code !=200:
              raise HTTPException(status_code=502,detail="fail to get the task")
          return response.json()
        except requests.RequestException:
            raise HTTPException(status_code=502,detail="External API request is fail")