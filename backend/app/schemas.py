from pydantic import BaseModel

class MovieBase(BaseModel):
    title: str

class MovieOut(MovieBase):
    id: int
    class Config:
        orm_mode = True

class InteractionIn(BaseModel):
    user_id: int
    movie_id: int
    rating: float