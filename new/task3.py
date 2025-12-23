#import librarie
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

#create app
task3 = FastAPI()

#To create user model
class User(BaseModel):
    name: str
    age:int
    email:str

#memory database
user_db=[]
current_id=1

#add user
@task3.post("/user")
def add(user:User):
    global current_id #function
    user_data=user.dict()
    user_data["id"]=current_id
    user_db.append(user_data)  #add unique id for user
    current_id+=1              #save user in list
    return{"message":"user is added","user":user_data}

#To get all user
@task3.get("/users")
def get():
    return user_db

#To get user by id
@task3.get("/user/{user_id}")
def get(user_id: int):  #id must be in integer
    for user in user_db:
        if user["id"] ==user_id:
            return user
        raise HTTPException(status_code=404,detail="user is not found") #if the no user found it display error