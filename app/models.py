from sqlalchemy import Column, Integer, String
from .database import Base

class Curso(Base):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    time = Column(Integer, index=True)