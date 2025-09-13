from sqlalchemy import Column, Integer, String
from database import Base

class CatFact(Base):
    __tablename__ = "catfacts"

    id = Column(Integer, primary_key=True, index=True)
    fact = Column(String, unique=True, index=True, nullable=False)
