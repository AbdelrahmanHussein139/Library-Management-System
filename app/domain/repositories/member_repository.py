from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID
from app.domain.models.member import Member

class MemberRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Member]:
        pass

    @abstractmethod
    def get_by_id(self, member_id: UUID) -> Optional[Member]:
        pass

    @abstractmethod
    def save(self, member: Member) -> Member:
        pass

    @abstractmethod
    def delete(self, member_id: UUID) -> None:
        pass
