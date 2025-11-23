from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import SessionLocal
from ..recommender import recommend_for_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/user/{user_id}")
def get_recommendations(user_id: int, db: Session = Depends(get_db)):
    ids = recommend_for_user(db, user_id)
    return {"user_id": user_id, "movie_ids": ids}