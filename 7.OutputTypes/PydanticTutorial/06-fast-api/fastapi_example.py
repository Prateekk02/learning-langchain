'''
Dependency Injection (via Depends) is used any time your route needs 
something that doesn't come from the request body or query parameters — like config, 
database, or the current user.

Think of it like this:
If it comes in the request body → Use a Pydantic model as a parameter.

If it comes from query/path → Use standard function parameters.

If it's a "background thing" (like settings, DB, user) → Use Depends() to fetch it from somewhere.

TL;DR
When your route needs something that's not passed by the client (like settings, DB, current user), 
use Depends() to inject it automatically — from config, env, database, or anywhere else.
'''


from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserSignUp(BaseModel):
    username: str
    email: EmailStr
    password: str
    
class Settings(BaseModel):
    app_name:str =  'Sherlock Cases'
    admin_mail: str = 'admin@sherlock.com'
    

# To make Settings as dependency injection

def get_settings():
    return Settings()

@app.post('/signup')
def signup(user: UserSignUp):
    return {"message": f"User {user.username} signed up successfully."}

@app.get('/settings')
def settings_endpoint(settings : Settings = Depends(get_settings)):
    return settings