from fastapi import Depends
from app.infrastructure.db.config import SessionLocal
from app.infrastructure.db.repositories.sqlalchemy_book_repository import SQLAlchemyBookRepository
from app.infrastructure.db.repositories.sqlalchemy_member_repository import SQLAlchemyMemberRepository
from app.application.services.book_service import BookService
from app.application.services.member_service import MemberService

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_book_service(db=Depends(get_db)):
    book_repo = SQLAlchemyBookRepository(db)
    member_repo = SQLAlchemyMemberRepository(db)
    return BookService(book_repo, member_repo)


def get_member_service(db=Depends(get_db)):
    member_repo = SQLAlchemyMemberRepository(db)
    return MemberService(member_repo)
