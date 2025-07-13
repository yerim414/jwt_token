from pydantic import BaseModel

class UserCreate(BaseModel):
    ID: str
    PWD: str
    NAME: str

class UserLogin(BaseModel):
    ID: str
    PWD: str