"""
define database tables and relations
"""

from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid
from datetime import datetime, timezone
from app.infrastructure.db.config import Base


class Member(Base):
    __tablename__ = "members"

    member_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False)

    # Establish one-to-many relationship: Member → Books
    borrowed_books = relationship("Book", back_populates="borrowed_by_member")


class Book(Base):
    __tablename__ = "books"

    book_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    author = Column(String(100), nullable=False)
    is_borrowed = Column(Boolean, default=False)
    borrowed_date = Column(DateTime, nullable=True)
    borrowed_by = Column(UUID(as_uuid=True), ForeignKey("members.member_id"), nullable=True)

    # Relationship back to Member
    borrowed_by_member = relationship("Member", back_populates="borrowed_books")

    def mark_as_borrowed(self, member_id: uuid.UUID):
        """
        Mark the book as borrowed by a specific member.
        """
        self.is_borrowed = True
        self.borrowed_by = member_id
        self.borrowed_date = datetime.now(timezone.utc)

    def mark_as_returned(self):
        """
        Mark the book as returned (make it available again).
        """
        self.is_borrowed = False
        self.borrowed_by = None
        self.borrowed_date = None
