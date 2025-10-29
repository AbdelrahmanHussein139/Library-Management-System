"""
Database configuration, Base Class For ORM Models
and session management.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.infrastructure.config import settings


# Base class for all ORM models.
Base = declarative_base()

engine = create_engine(
    settings.DATABASE_URL,
)

SessionLocal = sessionmaker(
    autocommit=False,  
    autoflush=False,   
    bind=engine     
)


def get_db():
    db = SessionLocal()
    try:
        yield db  
    finally:
        db.close()
