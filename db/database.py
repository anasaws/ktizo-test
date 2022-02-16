from config.config import settings
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine=create_engine(SQLALCHEMY_DATABASE_URL,
    echo=True
)

Base=declarative_base()
SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()