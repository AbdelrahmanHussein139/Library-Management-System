from datetime import datetime, timezone
from typing import List, Optional
from uuid import UUID
from fastapi import HTTPException, status
from app.infrastructure.db.repositories.sqlalchemy_book_repository import SQLAlchemyBookRepository
from app.infrastructure.db.repositories.sqlalchemy_member_repository import SQLAlchemyMemberRepository
from app.infrastructure.db.models import Book

class BookService:
    def __init__(self, book_repo: SQLAlchemyBookRepository, member_repo: SQLAlchemyMemberRepository):
        self.book_repo = book_repo
        self.member_repo = member_repo

    def get_all_books(self, skip=0, limit=10, search=None):
        return self.book_repo.get_all(skip=skip, limit=limit, search=search)

    def get_book_by_id(self, book_id: int) -> Optional[Book]:
        book = self.book_repo.get_by_id(book_id)
        if not book:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
        return book

    def create_book(self, title: str, author: str) -> Book:
        return self.book_repo.create(title=title, author=author)

    def update_book(self, book_id: int,updated_book:Book) -> Book:
        book=self.book_repo.get_by_id(book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        return self.book_repo.update(book_id,updated_book)

    def delete_book(self, book_id: int):
        book=self.book_repo.get_by_id(book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        self.book_repo.delete(book_id)

    def borrow_book(self, book_id: int, member_id: UUID) -> Book:
        book = self.get_book_by_id(book_id)
        if book.is_borrowed:
            raise HTTPException(status_code=400, detail="Book already borrowed")

        member = self.member_repo.get_by_id(member_id)
        if not member:
            raise HTTPException(status_code=404, detail="Member not found")

        book.is_borrowed = True
        book.borrowed_by = member_id
        book.borrowed_date = datetime.now(timezone.utc)
        return self.book_repo.save(book)

    def return_book(self, book_id: int) -> Book:
        book = self.get_book_by_id(book_id)
        if not book.is_borrowed:
            raise HTTPException(status_code=400, detail="Book is not borrowed")

        book.is_borrowed = False
        book.borrowed_by = None
        book.borrowed_date = None
        return self.book_repo.save(book)
