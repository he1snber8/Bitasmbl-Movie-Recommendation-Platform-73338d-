from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql://user:pass@localhost:5432/movies"

settings = Settings()