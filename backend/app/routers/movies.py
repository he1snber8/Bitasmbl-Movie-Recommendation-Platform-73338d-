from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import SessionLocal
from .. import models, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.MovieOut])
def list_movies(db: Session = Depends(get_db)):
    return db.query(models.Movie).all()

@router.post("/interactions")
def add_interaction(payload: schemas.InteractionIn, db: Session = Depends(get_db)):
    obj = models.UserInteraction(**payload.dict())
    db.add(obj)
    db.commit()
    return {"id": obj.id}