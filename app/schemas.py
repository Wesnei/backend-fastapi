from typing import Optional

from pydantic import BaseModel

class CursoBase (BaseModel):
    name: str
    description: str
    time: int

class CursoCreate(CursoBase):
    pass

class CursoUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    time: Optional[int]

class Curso(CursoBase):
    id: int

    class Config:
        from_attributes = True
