#import module
import requests
from fastapi import FastAPI,HTTPException

#create app
taske2=FastAPI()

@taske2.get("/random-user")
def random():
    try:
        response=requests.get("https://randomuser.me/api/",timeout=5)

        #check API response is ok
        if response.status_code !=200:
            raise HTTPException(500,"invalid API response")
        
        #convert response to json
        data=response.json()

        #it return user data
        return data["results"][0]
    #if API is slow
    except requests.exceptions.Timeout:
        raise HTTPException(504,"request timeout")
    
    #if APi is not reach
    except requests.exceptions.ConnectionError:
        raise HTTPException(502,"cannot connect with API")
    
    #other error
    except Exception:
        raise HTTPException(500,"something is went wrong")
