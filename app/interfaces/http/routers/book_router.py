from fastapi import APIRouter, Depends, HTTPException, status, Query
from uuid import UUID
from typing import List
from typing import Optional

from app.application.services.book_service import BookService
from app.interfaces.http.dependencies import get_book_service
from app.application.dto.book_dto import (
    BookCreate,
    BookUpdate,
    BookResponse,
)

router = APIRouter()


@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(dto: BookCreate, service: BookService = Depends(get_book_service)):
    return service.create_book(dto.title, dto.author)


@router.get("/", response_model=list[BookResponse])
def get_all_books(
    skip: int = 0,
    limit: int = 10,
    search: Optional[str] = Query(None, description="Search by title or author"),
    service: BookService = Depends(get_book_service),
):
    return service.get_all_books(skip=skip, limit=limit, search=search)



@router.get("/{book_id}", response_model=BookResponse)
def get_book_by_id(book_id: int, service: BookService = Depends(get_book_service)):
    book = service.get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.put("/{book_id}", response_model=BookResponse)
def update_book(
    book_id: int,
    dto: BookUpdate,
    service: BookService = Depends(get_book_service),
):
    updated = service.update_book(book_id, dto)
    if not updated:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, service: BookService = Depends(get_book_service)):
    deleted = service.delete_book(book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return


@router.post("/borrow/{book_id}/{member_id}", response_model=BookResponse)
def borrow_book(book_id: int, member_id: UUID, service: BookService = Depends(get_book_service)):
    try:
        book = service.borrow_book(book_id, member_id)
        return book
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/return/{book_id}", response_model=BookResponse)
def return_book(book_id: int, service: BookService = Depends(get_book_service)):
    try:
        book = service.return_book(book_id)
        return book
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
