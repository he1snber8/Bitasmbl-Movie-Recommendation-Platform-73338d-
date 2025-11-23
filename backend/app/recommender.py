import tensorflow as tf
from sqlalchemy.orm import Session
from . import models

def recommend_for_user(db: Session, user_id: int, limit: int = 10):
    # placeholder for training/inference logic
    movies = db.query(models.Movie).limit(limit).all()
    return [m.id for m in movies]