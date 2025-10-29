from typing import List, Optional
from fastapi import HTTPException, status
from uuid import UUID
from app.infrastructure.db.repositories.sqlalchemy_member_repository import SQLAlchemyMemberRepository
from app.infrastructure.db.models import Member


class MemberService:
    def __init__(self, member_repo: SQLAlchemyMemberRepository):
        self.member_repo = member_repo

    def get_all_members(self, skip=0, limit=10, search=None):
        return self.member_repo.get_all(skip=skip, limit=limit, search=search)


    def get_member_by_id(self, member_id: UUID) -> Optional[Member]:
        member = self.member_repo.get_by_id(member_id)
        if not member:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Member not found")
        return member

    def create_member(self, name: str, email: str) -> Member:
        existing = self.member_repo.get_by_email(email)
        if existing:
            raise HTTPException(status_code=400, detail="Email already exists")
        return self.member_repo.create(name, email)

    def update_member(self, member_id: UUID,updated_member:Member) -> Member:
        member = self.member_repo.get_by_id(member_id)
        if not member:
            raise HTTPException(status_code=404, detail="Member not found")
        return self.member_repo.update(member_id,updated_member)

    def delete_member(self, member_id: UUID):
        member = self.member_repo.get_by_id(member_id)
        if not member:
            raise HTTPException(status_code=404, detail="Member not found")
        self.member_repo.delete(member_id)
