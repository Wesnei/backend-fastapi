from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db
import logging

logger = logging.getLogger(__name__)

router = APIRouter()



@router.get("/alunos", response_model=list[schemas.Aluno])
def read_alunos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        alunos = crud.get_alunos(db, skip=skip, limit=limit)
        return alunos
    except Exception as e:
        logger.error(f"Erro inesperado: {e}")
        raise HTTPException(status_code=500, detail="Erro inesperado ao listar os alunos.")

@router.get("/alunos/{aluno_id}", response_model=schemas.Aluno)
def read_aluno(aluno_id: int, db: Session = Depends(get_db)):
    try:
        db_aluno = crud.get_aluno(db, aluno_id=aluno_id)
        if db_aluno is None:
            raise HTTPException(status_code=404, detail="Aluno não encontrado")
        return db_aluno
    except Exception as e:
        logger.error(f"Erro inesperado: {e}")
        raise HTTPException(status_code=500, detail="Erro inesperado ao buscar o aluno.")

@router.post("/alunos", response_model=schemas.Aluno)
def create_aluno(aluno: schemas.AlunoCreate, db: Session = Depends(get_db)):
    try:
        if not aluno.nome or aluno.idade is None or not aluno.email:
            raise HTTPException(status_code=400, detail="Todos os campos são obrigatórios.")
        return crud.create_aluno(db=db, aluno=aluno)
    except Exception as e:
        logger.error(f"Erro inesperado: {e}")
        raise HTTPException(status_code=500, detail="Erro inesperado ao criar o aluno.")

@router.put("/alunos/{aluno_id}", response_model=schemas.Aluno)
def update_aluno(aluno_id: int, aluno: schemas.AlunoUpdate, db: Session = Depends(get_db)):
    try:
        db_aluno = crud.get_aluno(db, aluno_id=aluno_id)
        if db_aluno is None:
            raise HTTPException(status_code=404, detail="Aluno não encontrado")
        updated_aluno = crud.update_aluno(db=db, aluno_id=aluno_id, aluno=aluno)
        return updated_aluno
    except Exception as e:
        logger.error(f"Erro inesperado: {e}")
        raise HTTPException(status_code=500, detail="Erro inesperado ao atualizar o aluno.")

@router.delete("/alunos/{aluno_id}")
def delete_aluno(aluno_id: int, db: Session = Depends(get_db)):
    try:
        db_aluno = crud.get_aluno(db, aluno_id=aluno_id)
        if db_aluno is None:
            raise HTTPException(status_code=404, detail="Aluno não encontrado")
        crud.delete_aluno(db=db, aluno_id=aluno_id)
        return {"detail": "Aluno removido com sucesso"}
    except Exception as e:
        logger.error(f"Erro inesperado: {e}")
        raise HTTPException(status_code=500, detail="Erro inesperado ao remover o aluno.")

