import logging
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import engine, get_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

models.Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)

@app.get("/")
def welcome_message():
    return "Welcome to the API"

@app.get("/cursos/", response_model=list[schemas.Curso])
def read_cursos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        cursos = crud.get_items(db, skip=skip, limit=limit)
        return cursos

    except Exception as e:
        logger.error(f"Erro inesperado: {e}")
        raise HTTPException(status_code=500, detail="Erro inesperado ao listar os cursos.")

@app.get("/cursos/{curso_id}", response_model=schemas.Curso)
def read_curso(curso_id: int, db: Session = Depends(get_db)):

    try:
        db_curso = crud.get_item(db, item_id=curso_id)
        if db_curso is None:
            raise HTTPException(status_code=404, detail="Curso não encontrado")
        return db_curso

    except Exception as e:
        logger.error(f"Erro inesperado: {e}")
        raise HTTPException(status_code=500, detail="Erro inesperado ao buscar o curso.")


@app.post("/cursos/", response_model=schemas.Curso)
def create_curso(curso: schemas.CursoCreate, db: Session = Depends(get_db)):
    try:
        if not curso.name or not curso.description or curso.time is None:
            raise HTTPException(status_code=400, detail="Todos os campos são obrigatórios.")

        return crud.create_item(db=db, item=curso)

    except Exception as e:
        logger.error(f"Erro inesperado: {e}")
        raise HTTPException(status_code=500, detail="Erro inesperado ao criar o curso.")