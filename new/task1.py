#import fastapi
from fastapi import FastAPI  

#It create API app
task1=FastAPI()

#To get API endpoint
@task1.get("/")
def hello():     #function name
    return{"message" : "hello"}   #send response message

#Another endpoint
@task1.get("/task")
def task():       #function name
    return{"message": "welcome"}   #send response message