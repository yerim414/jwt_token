from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from models.user_model import User
from schemas.user_schemas import UserCreate
from passlib.hash import bcrypt

app = FastAPI()

@app.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.ID == user.ID).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="이미 존재하는 ID 입니다.")
    
    # TODO : 서비스로 옮기기
    hashed_pwd = bcrypt.hash(user.PWD)
    new_user = User(
        ID = user.ID,
        PWD = hashed_pwd,
        NAME = user.NAME
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"code":201,"user_seq": new_user.SEQ}
