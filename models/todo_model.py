from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db import Base

class ToDo(Base):
    __tablename__ = "todos"

    SEQ = Column(Integer, primary_key=True, index=True)
    TITLE = Column(String(100), nullable=False)
    DESCRIPTION = Column(String(255), nullable=True)
    COMPLETED = Column(Boolean, default=False)
    CREATED_AT = Column(DateTime, nullable=False, server_default=func.now())
    DELETED_AT = Column(DateTime, nullable=True)

    # 작성자
    ID = Column(Integer, ForeignKey("user.SEQ"), nullable=False)
    OWNER = relationship("User", back_populates="todos")

    # ID : 실제 DB 테이블에 틀어가는 컬럼
    # ToDo 객체에서 .OWNER 속성을 접근하면, 자동으로 연결된 User 객체를 불러올 수 있음.