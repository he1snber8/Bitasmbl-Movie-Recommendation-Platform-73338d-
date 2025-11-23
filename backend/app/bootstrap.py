from fastapi import FastAPI
from .routers import movies, recommendations
from .cors import setup_cors

def create_app() -> FastAPI:
    app = FastAPI(title="Movie Recommendation Platform")
    setup_cors(app)
    app.include_router(movies.router, prefix="/movies")
    app.include_router(recommendations.router, prefix="/recommendations")
    return app