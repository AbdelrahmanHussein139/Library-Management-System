"""
Base module for SQLAlchemy models.
"""
# Import the Base class (declarative base) from the config
from app.infrastructure.db.config import Base

# Import all models so Alembic can see them
from app.infrastructure.db.models import Book, Member

# Expose metadata for Alembic
__all__ = ["Base", "Book", "Member"]
