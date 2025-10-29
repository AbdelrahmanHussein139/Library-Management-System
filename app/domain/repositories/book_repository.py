from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID
from app.domain.models.book import Book

class BookRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Book]:
        pass

    @abstractmethod
    def get_by_id(self, book_id: int) -> Optional[Book]:
        pass

    @abstractmethod
    def save(self, book: Book) -> Book:
        pass

    @abstractmethod
    def delete(self, book_id: int) -> None:
        pass
