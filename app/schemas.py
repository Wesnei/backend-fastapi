from typing import Optional
from pydantic import BaseModel


class CursoBase(BaseModel):
    name: str
    description: str
    time: int

class CursoCreate(CursoBase):
    pass

class CursoUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    time: Optional[int] = None

class Curso(CursoBase):
    id: int

    class Config:
        from_attributes = True


class AlunoBase(BaseModel):
    nome: str
    idade: int


class AlunoCreate(AlunoBase):
    pass

class AlunoUpdate(BaseModel):
    nome: Optional[str] = None
    idade: Optional[int] = None

class Aluno(AlunoBase):
    id: int

    class Config:
        from_attributes = True


class ProfessorBase(BaseModel):
    nome: str
    disciplina: str

class ProfessorCreate(ProfessorBase):
    pass

class ProfessorUpdate(BaseModel):
    nome: Optional[str] = None
    disciplina: Optional[str] = None

class Professor(ProfessorBase):
    id: int

    class Config:
        from_attributes = True
