from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db
import logging

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/professores", response_model=list[schemas.Professor])
def read_professores(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        professores = crud.get_professores(db, skip=skip, limit=limit)
        return professores
    except Exception as e:
        logger.error(f"Erro inesperado: {e}")
        raise HTTPException(status_code=500, detail="Erro inesperado ao listar os professores.")

@router.get("/professores/{professor_id}", response_model=schemas.Professor)
def read_professor(professor_id: int, db: Session = Depends(get_db)):
    try:
        db_professor = crud.get_professor(db, professor_id=professor_id)
        if db_professor is None:
            raise HTTPException(status_code=404, detail="Professor não encontrado")
        return db_professor
    except Exception as e:
        logger.error(f"Erro inesperado: {e}")
        raise HTTPException(status_code=500, detail="Erro inesperado ao buscar o professor.")

@router.post("/professores", response_model=schemas.Professor)
def create_professor(professor: schemas.ProfessorCreate, db: Session = Depends(get_db)):
    try:
        if not professor.nome or not professor.disciplina or not professor.email:
            raise HTTPException(status_code=400, detail="Todos os campos são obrigatórios.")
        return crud.create_professor(db=db, professor=professor)
    except Exception as e:
        logger.error(f"Erro inesperado: {e}")
        raise HTTPException(status_code=500, detail="Erro inesperado ao criar o professor.")

@router.put("/professores/{professor_id}", response_model=schemas.Professor)
def update_professor(professor_id: int, professor: schemas.ProfessorUpdate, db: Session = Depends(get_db)):
    try:
        db_professor = crud.get_professor(db, professor_id=professor_id)
        if db_professor is None:
            raise HTTPException(status_code=404, detail="Professor não encontrado")
        updated_professor = crud.update_professor(db=db, professor_id=professor_id, professor=professor)
        return updated_professor
    except Exception as e:
        logger.error(f"Erro inesperado: {e}")
        raise HTTPException(status_code=500, detail="Erro inesperado ao atualizar o professor.")

@router.delete("/professores/{professor_id}")
def delete_professor(professor_id: int, db: Session = Depends(get_db)):
    try:
        db_professor = crud.get_professor(db, professor_id=professor_id)
        if db_professor is None:
            raise HTTPException(status_code=404, detail="Professor não encontrado")
        crud.delete_professor(db=db, professor_id=professor_id)
        return {"detail": "Professor removido com sucesso"}
    except Exception as e:
        logger.error(f"Erro inesperado: {e}")
        raise HTTPException(status_code=500, detail="Erro inesperado ao remover o professor.")