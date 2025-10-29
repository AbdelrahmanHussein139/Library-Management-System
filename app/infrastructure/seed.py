"""
Seed the database with initial data for testing or development.
"""
from datetime import datetime, timezone
from sqlalchemy.orm import Session
from app.infrastructure.db.config import SessionLocal
from app.infrastructure.db import models


def seed():
    db: Session = SessionLocal()

    # Check if already seeded
    existing_books = db.query(models.Book).count()
    existing_members = db.query(models.Member).count()

    if existing_books == 0 and existing_members == 0:
        # Create some members
        member1 = models.Member(name="Alice Johnson", email="alice@example.com")
        member2 = models.Member(name="Bob Smith", email="bob@example.com")

        # Create some books
        book1 = models.Book(title="The Pragmatic Programmer", author="Andrew Hunt")
        book2 = models.Book(title="Clean Code", author="Robert C. Martin")
        book3 = models.Book(title="FastAPI Deep Dive", author="John Doe")

        db.add_all([member1, member2, book1, book2, book3])
        db.commit()
        print("Database seeded successfully.")
    else:
        print("Database already contains data — skipping seeding.")

    db.close()


if __name__ == "__main__":
    seed()
