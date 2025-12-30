#importn module
from fastapi import FastAPI

#create app
taskb2 = FastAPI()

#expense list
expenses=[
    {"category":"Food","amount":500},
    {"category":"transport","amount":200},
    {"category":"Food","amount":300},
    {"category":"shopping","amount":1000}
]

#get endpoint
@taskb2.get("/expenses/categories")
def count():
    result={}
    for expense in expenses:
        category=expense["category"]
        if category in result:
            result[category]+=1
        else:
            result[category]=1

    #return result
    return result 