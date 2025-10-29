from app.domain.models.book import Book

class BorrowPolicy:
    """Business rules for borrowing a book."""

    @staticmethod
    def can_borrow(book: Book) -> bool:
        return not book.is_borrowed
