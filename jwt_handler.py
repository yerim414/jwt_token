from dotenv import load_dotenv
import os
import datetime
import jwt
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from db import SessionLocal
from models.user_model import User

security = HTTPBearer(auto_error=False)

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"


def create_token(data: dict, exp_time: int = 30):
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=exp_time)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token


def decode_token(token: str):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded
    except ExpiredSignatureError:
        return {"error": "Token has expired"}
    except InvalidTokenError:
        return {"error": "Invalid token"}
    
def auth_check(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials is None:
        raise HTTPException(status_code=401, detail="권한이 없습니다. 인증 토큰을 제공하세요.")

    token = credentials.credentials
    try:
        payload = decode_token(token)
        user_id = payload.get("user_id")
        db = SessionLocal()
        user = db.query(User).filter(User.SEQ == user_id).first()
        db.close()

        if user is None:
            raise HTTPException(status_code=401, detail="유효하지 않은 토큰입니다.")
        return user

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="토큰이 만료되었습니다.")
    except Exception:
        raise HTTPException(status_code=401, detail="유효하지 않은 토큰입니다.")