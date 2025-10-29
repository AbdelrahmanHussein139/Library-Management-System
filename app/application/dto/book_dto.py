from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from uuid import UUID


class BookBase(BaseModel):
    title: str
    author: str


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    is_borrowed: Optional[bool] = None
    borrowed_by: Optional[UUID] = None


class BookResponse(BookBase):
    book_id: int
    is_borrowed: bool
    borrowed_date: Optional[datetime] = None
    borrowed_by: Optional[UUID] = None

    class Config:
        orm_mode = True  
