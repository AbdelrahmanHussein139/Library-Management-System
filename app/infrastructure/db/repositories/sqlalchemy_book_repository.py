from sqlalchemy.orm import Session
from app.infrastructure.db.models import Book
from typing import List, Optional
from uuid import UUID

class SQLAlchemyBookRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 10, search: Optional[str] = None) -> List[Book]:
        query = self.db.query(Book)
        if search:
            query = query.filter(
                (Book.title.ilike(f"%{search}%")) | (Book.author.ilike(f"%{search}%"))
            )
        return query.offset(skip).limit(limit).all()

    def get_by_id(self, book_id: int) -> Optional[Book]:
        return self.db.query(Book).filter(Book.book_id == book_id).first()

    def create(self, title: str, author: str) -> Book:
        book = Book(title=title, author=author)
        self.db.add(book)
        self.db.commit()
        self.db.refresh(book)
        return book

    def update(self,book_id:int,updated_book:Book):
        book=self.get_by_id(book_id)
        if book:
         book.author=updated_book.author
         book.title=updated_book.title
         self.db.add(book)
         self.db.commit()
         self.db.refresh(book)
         return book

    def delete(self, book_id: int):
        book = self.get_by_id(book_id)
        if book:
            self.db.delete(book)
            self.db.commit()
    
    def save(self, book: Book) -> Book:
      self.db.add(book)
      self.db.commit()
      self.db.refresh(book)
      return book