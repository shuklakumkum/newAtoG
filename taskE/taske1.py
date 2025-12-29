#import module
from fastapi import FastAPI,HTTPException

#create app
taske1=FastAPI()

#it check if parameter are missing
@taske1.get("/calculate/divide")
def divide(a:int=None,b:int=None):
    if a is None or b is None:
        raise HTTPException(status_code=400,detail="both parameter is required")
    
    if b==0:  #check b is divide by zero
        raise HTTPException(status_code=400,detail="cannot be devided by zero")
    
    #it perform division
    result=a/b

    #return result
    return{"result":result}
