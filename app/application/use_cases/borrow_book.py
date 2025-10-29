from datetime import datetime, timezone
from uuid import UUID

from app.infrastructure.db.repositories.sqlalchemy_book_repository import SQLAlchemyBookRepository
from app.infrastructure.db.repositories.sqlalchemy_member_repository import SQLAlchemyMemberRepository
from app.infrastructure.db.models import Book


class BorrowBookUseCase:
    """Use case: borrow a book for a member."""

    def __init__(self, book_repo: SQLAlchemyBookRepository, member_repo: SQLAlchemyMemberRepository):
        self.book_repo = book_repo
        self.member_repo = member_repo

    def execute(self, book_id: int, member_id: UUID) -> Book:
        # 1️⃣ Get the book
        book = self.book_repo.get_by_id(book_id)
        if not book:
            raise ValueError("Book not found")

        # 2️⃣ Check if it's already borrowed
        if book.is_borrowed:
            raise ValueError("Book is already borrowed")

        # 3️⃣ Validate member exists
        member = self.member_repo.get_by_id(member_id)
        if not member:
            raise ValueError("Member not found")

        # 4️⃣ Update book state
        book.is_borrowed = True
        book.borrowed_by = member.member_id
        book.borrowed_date = datetime.now(timezone.utc)

        # 5️⃣ Save changes
        return self.book_repo.update(book)
