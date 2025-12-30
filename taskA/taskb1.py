#import model
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

#create app
taskb1=FastAPI()

class TaskB(BaseModel):
    name:str
    email:str

#store added person
member=[]

#post endpoint
@taskb1.post("/person")
def add(person:TaskB):
    for existing in member:
        if existing.email == person.email:
            raise HTTPException(status_code=400,detail="email is already exist")
        
    #add new person
    member.append(person)
    
    #success message
    return{"success":"true","message":f"person {person.name} add successfully"}