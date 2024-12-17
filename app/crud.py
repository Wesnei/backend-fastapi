from sqlalchemy.orm import Session
from . import models, schemas


def get_curso(db: Session, curso_id: int):
    return db.query(models.Curso).filter(models.Curso.id == curso_id).first()

def get_cursos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Curso).offset(skip).limit(limit).all()

def create_curso(db: Session, curso: schemas.CursoCreate):
    db_curso = models.Curso(name=curso.name, description=curso.description, time=curso.time)
    db.add(db_curso)
    db.commit()
    db.refresh(db_curso)
    return db_curso

def update_curso(db: Session, curso_id: int, curso: schemas.CursoUpdate):
    db_curso = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    if db_curso:
        for key, value in curso.dict(exclude_unset=True).items():
            setattr(db_curso, key, value)
        db.commit()
        db.refresh(db_curso)
        return db_curso

def delete_curso(db: Session, curso_id: int):
    db_curso = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    if db_curso:
        db.delete(db_curso)
        db.commit()


def get_aluno(db: Session, aluno_id: int):
    return db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()

def get_alunos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Aluno).offset(skip).limit(limit).all()

def create_aluno(db: Session, aluno: schemas.AlunoCreate):
    db_aluno = models.Aluno(nome=aluno.nome, idade=aluno.idade, email=aluno.email)
    db.add(db_aluno)
    db.commit()
    db.refresh(db_aluno)
    return db_aluno

def update_aluno(db: Session, aluno_id: int, aluno: schemas.AlunoUpdate):
    db_aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
    if db_aluno:
        for key, value in aluno.dict(exclude_unset=True).items():
            setattr(db_aluno, key, value)
        db.commit()
        db.refresh(db_aluno)
        return db_aluno

def delete_aluno(db: Session, aluno_id: int):
    db_aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
    if db_aluno:
        db.delete(db_aluno)
        db.commit()


def get_professor(db: Session, professor_id: int):
    return db.query(models.Professor).filter(models.Professor.id == professor_id).first()

def get_professores(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Professor).offset(skip).limit(limit).all()

def create_professor(db: Session, professor: schemas.ProfessorCreate):
    db_professor = models.Professor(nome=professor.nome, disciplina=professor.disciplina, email=professor.email)
    db.add(db_professor)
    db.commit()
    db.refresh(db_professor)
    return db_professor

def update_professor(db: Session, professor_id: int, professor: schemas.ProfessorUpdate):
    db_professor = db.query(models.Professor).filter(models.Professor.id == professor_id).first()
    if db_professor:
        for key, value in professor.dict(exclude_unset=True).items():
            setattr(db_professor, key, value)
        db.commit()
        db.refresh(db_professor)
        return db_professor

def delete_professor(db: Session, professor_id: int):
    db_professor = db.query(models.Professor).filter(models.Professor.id == professor_id).first()
    if db_professor:
        db.delete(db_professor)
        db.commit()
