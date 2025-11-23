from fastapi import FastAPI
from .routers import movies

app = FastAPI(title="Movie Recommendation Platform")

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(movies.router, prefix="/movies", tags=["movies"])