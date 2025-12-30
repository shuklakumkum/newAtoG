#import module
from fastapi import FastAPI,HTTPException

#create app
task =FastAPI()

#user data
users=[
    {"id":1, "name":"Alice","email":"alice@test.com"},
    {"id":2, "name":"Bob","email":"bob@test.com"},
    {"id":3, "name":"Charlie","email":"charlie@test.com"}
]

#get endpoint
@task.get("/user/email/{email}")
def get(email: str):
    for user in users:
        if user["email"] == email:
            return user

#error after loop
    raise HTTPException(status_code=404,detail="user cannot be found")
    