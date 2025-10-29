from datetime import datetime, timezone
from uuid import UUID
from typing import Optional

class Book:
    def __init__(self, book_id: int, title: str, author: str, is_borrowed: bool = False,
                 borrowed_date: Optional[datetime] = None, borrowed_by: Optional[UUID] = None):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
        self.borrowed_date = borrowed_date
        self.borrowed_by = borrowed_by

    def borrow(self, member_id: UUID):
        if self.is_borrowed:
            raise ValueError("Book already borrowed")
        self.is_borrowed = True
        self.borrowed_date = datetime.now(timezone.utc)
        self.borrowed_by = member_id

    def return_book(self):
        if not self.is_borrowed:
            raise ValueError("Book is not borrowed")
        self.is_borrowed = False
        self.borrowed_date = None
        self.borrowed_by = None
