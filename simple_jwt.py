import jwt
import datetime

SECRET_KEY = "mysecretkey"

# 토큰 생성
payload = {
    "user_id": 123,
    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)  # 만료시간
}
token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
print(f"Generated Token: {token}")

# 토큰 검증 및 디코딩
try:
    decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    print("Decoded Payload:", decoded)
except jwt.ExpiredSignatureError:
    print("Token has expired.")
except jwt.InvalidTokenError:
    print("Invalid token.")

# 소스 Info
# https://www.notion.so/JWT-2215505d65de8081bdb3ec591833eb44