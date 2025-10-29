from sqlalchemy.orm import Session
from app.infrastructure.db.models import Member
from typing import List, Optional
from uuid import UUID

class SQLAlchemyMemberRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 10, search: Optional[str] = None) -> List[Member]:
        query = self.db.query(Member)
        if search:
            query = query.filter(
                (Member.name.ilike(f"%{search}%")) | (Member.email.ilike(f"%{search}%"))
            )
        return query.offset(skip).limit(limit).all()

    def get_by_id(self, member_id: UUID) -> Optional[Member]:
        return self.db.query(Member).filter(Member.member_id == member_id).first()

    def get_by_email(self, email: str) -> Optional[Member]:
        return self.db.query(Member).filter(Member.email == email).first()

    def create(self, name: str, email: str) -> Member:
        member = Member(name=name, email=email)
        self.db.add(member)
        self.db.commit()
        self.db.refresh(member)
        return member

    def update(self,member_id: UUID,updated_member: Member):
        member = self.get_by_id(member_id)
        if member:
         member.email=updated_member.email
         member.name=updated_member.name
         self.db.add(member)
         self.db.commit()
         self.db.refresh(member)
         return member
        

    def delete(self, member_id: UUID)->bool:
        member = self.get_by_id(member_id)
        if member:
            self.db.delete(member)
            self.db.commit()
            return True
        return False
