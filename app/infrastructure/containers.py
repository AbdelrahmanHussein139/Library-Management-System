from dependency_injector import containers, providers
from app.infrastructure.db.config import SessionLocal
from app.infrastructure.db.repositories.sqlalchemy_book_repository import SQLAlchemyBookRepository
from app.infrastructure.db.repositories.sqlalchemy_member_repository import SQLAlchemyMemberRepository
from app.application.services.book_service import BookService
from app.application.services.member_service import MemberService

class Container(containers.DeclarativeContainer):
    """Dependency Injection Container for the entire app."""

    wiring_config = containers.WiringConfiguration(
        packages=["app.interfaces.http.routers"]
    )

    # Database session factory
    db_session = providers.Factory(SessionLocal)

    # Repositories
    book_repository = providers.Factory(
        SQLAlchemyBookRepository,
        db_session=db_session
    )

    member_repository = providers.Factory(
        SQLAlchemyMemberRepository,
        db_session=db_session
    )

    # Services
    book_service = providers.Factory(
        BookService,
        book_repository=book_repository
    )

    member_service = providers.Factory(
        MemberService,
        member_repository=member_repository
    )
