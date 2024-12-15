from sqlalchemy.orm import Session
from . import models, schemas

def get_item(db: Session, item_id: int):
    return db.query(models.Curso).filter(models.Curso.id == item_id).first()

def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Curso).offset(skip).limit(limit).all()

def create_item(db: Session, item: schemas.CursoCreate):
    db_item = models.Curso(name=item.name, description=item.description, time=item.time)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item