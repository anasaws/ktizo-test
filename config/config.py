import os

class Settings:
    PROJECT_TITLE: str = "Ktizo"
    PROJECT_VERSION: str = "0.0.1"
    POSTGRES_USER: str = "ktizo"
    POSTGRES_PASSWORD: str = "ktizo"
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: str = "5432"
    POSTGRES_DB: str = "ktizodb"
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"
    ALGORITHM = "HS256"
    SECRET_KEY: str = "de848c1c8a8de5afc65c88b12da0edda"


    
settings = Settings()