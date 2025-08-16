# JWT Token FastAPI 프로젝트

## 프로젝트 개요
FastAPI와 JWT를 이용한 사용자 인증/인가 시스템 구현 프로젝트입니다.  
- 회원가입(Sign Up)  
- 로그인(Login) → JWT 토큰 발급  
- 인증된 사용자 정보 조회(`/me`)

## 사용 기술
- Python 3.10+ / FastAPI / SQLAlchemy  
- JWT(PyJWT) / Passlib(Bcrypt) / dotenv

## ⚠️ 환경 주의 사항
- DB 연결: 각자 환경에 맞게 `DB_URL` 설정 필요  
  - 예: `mysql+pymysql://user:password@localhost/db_name`  
- Python 가상환경 권장  
- SECRET_KEY는 각자 .env 파일에서 안전하게 설정  

- ## 실행 방법
1. 가상환경 생성
```bash
python -m venv .venv
source .venv/bin/activate  # Linux / Mac
.venv\Scripts\activate     # Windows
```

2. 패키지 설치
```bash
pip install -r requirements.txt
```

3. 환경변수(.env) 설정
```bash
SECRET_KEY=your_secret_key
DB_URL=mysql+pymysql://user:password@localhost/db_name
```

4. 서버 실행
```bash
python main.py
```

5. swagger 접속
```bash
http://localhost:8000/docs#
```

