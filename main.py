from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from models.user_model import User
from schemas.user_schemas import UserCreate, UserLogin
from passlib.hash import bcrypt
from services.user_service import create_user, login_user

app = FastAPI()

@app.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    new_user = create_user(user, db)
    if user is None:
        raise HTTPException(status_code=400, detail = "생성에 실패하였습니다.")
    return {"code":201,"user_seq": new_user.SEQ}

@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    return login_user(user, db)
