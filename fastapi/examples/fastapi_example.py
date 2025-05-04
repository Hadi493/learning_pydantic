from fastapi import FastAPI, Depends # type: ignore
from pydantic import BaseModel, EmailStr # type: ignore


app = FastAPI()

class UserSignup(BaseModel):
    username: str
    email: EmailStr
    password: str

class Settings(BaseModel):
    app_name: str
    admin_email: str = "admin@example.com"

def get_settings():
    return Settings()

@app.post('/signup')
def signup(user: UserSignup):
    return {'massage': f'User {user.username} created successfully'}

@app.get('/settings')
def get_settings_endpoint(settings: Settings = Depends(get_settings)):
    return settings
