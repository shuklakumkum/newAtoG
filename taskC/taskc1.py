#import module
from fastapi import FastAPI
from pydantic import BaseModel

#create app
taskc1=FastAPI()

class Task(BaseModel):
    title:str
    completed:bool=False

#To store task
tasks=[]

#global id counter
next_id=1

#It create task
@taskc1.post("/tasks")
def create(task:Task):
    global next_id

  #create task with id
    new_task={
        "id":next_id,
        "title":task.title,
        "completed":task.completed       
   }
    
    #add task
    tasks.append(new_task)

    #increase id
    next_id=next_id+1

    #return task
    return new_task

#c2: delete
@taskc1.delete("/tasks/reset")
def reset_tasks():
    global next_id
    tasks.clear()
    next_id=1
    return{
        "message":"All task is deleted",
        "next_id":next_id
    }