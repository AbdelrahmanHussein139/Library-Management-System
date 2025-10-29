from pydantic import BaseModel, EmailStr
from uuid import UUID


class MemberBase(BaseModel):
    name: str
    email: EmailStr


class MemberCreate(MemberBase):
    pass


class MemberUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None


class MemberResponse(MemberBase):
    member_id: UUID

    class Config:
        orm_mode = True
