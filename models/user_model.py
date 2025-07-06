from sqlalchemy import Column, Integer, String, DateTime
from db import Base

class User(Base):
    __tablename__ = "user"

    SEQ = Column(Integer, primary_key=True, index=True)
    ID = Column(String(50), unique=True, nullable=False)
    PWD = Column(String(50), nullable=False)
    NAME = Column(String(50), nullable=False)
    DELETED_AT = Column(DateTime, nullable=True)