from sqlalchemy.orm import Session
from jwt_handler import create_token
from models.user_model import User
from schemas.user_schemas import UserCreate, UserLogin
from passlib.hash import bcrypt
from fastapi import HTTPException
from db import get_db

def create_user(user: UserCreate, db: Session) -> User:
    # ID 중복 확인
    existing_user = db.query(User).filter(User.ID == user.ID).first()
    if existing_user:
        # raise HTTPException(status_code=400, detail="이미 존재하는 ID 입니다.")
        return None
    
    # 비밀번호 해싱
    hashed_pwd = bcrypt.hash(user.PWD)

    new_user = User(
        ID=user.ID,
        PWD=hashed_pwd,
        NAME=user.NAME
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def login_user(user: UserLogin, db: Session):
    db_user = db.query(User).filter(User.ID == user.ID).first()
    if not db_user:
        raise HTTPException(status_code=401, detail="존재하지 않는 ID입니다.")
    
    if not bcrypt.verify(user.PWD, db_user.PWD):
        raise HTTPException(status_code=401, detail="비밀번호가 일치하지 않습니다.")
    
    access_token = create_token(data={"user_id": db_user.SEQ})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }