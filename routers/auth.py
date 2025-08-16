from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from jwt_handler import auth_check
from models.user_model import User
from schemas.user_schemas import UserCreate, UserLogin
from services.user_service import create_user, login_user

router = APIRouter(prefix="", tags=["Auth"])

@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    new_user = create_user(user, db)

    if new_user is None:
        raise HTTPException(status_code=400, detail="생성에 실패하였습니다.")

    return {"code": 201, "user_seq": new_user.SEQ}

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    return login_user(user, db)

@router.get("/me")
def read_users_me(current_user: User = Depends(auth_check)):
    return {
        "SEQ": current_user.SEQ,
        "ID": current_user.ID,
        "NAME": current_user.NAME,
        "desc": "인증에 성공함!"
    }