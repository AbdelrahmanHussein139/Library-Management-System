from app.infrastructure.db.repositories.sqlalchemy_book_repository import SQLAlchemyBookRepository
from app.infrastructure.db.models import Book


class ReturnBookUseCase:
    """Use case: return a borrowed book."""

    def __init__(self, book_repo: SQLAlchemyBookRepository):
        self.book_repo = book_repo

    def execute(self, book_id: int) -> Book:
        # 1️⃣ Fetch book
        book = self.book_repo.get_by_id(book_id)
        if not book:
            raise ValueError("Book not found")

        # 2️⃣ Ensure it was borrowed
        if not book.is_borrowed:
            raise ValueError("Book is not currently borrowed")

        # 3️⃣ Reset fields
        book.is_borrowed = False
        book.borrowed_by = None
        book.borrowed_date = None

        # 4️⃣ Save
        return self.book_repo.update(book)
