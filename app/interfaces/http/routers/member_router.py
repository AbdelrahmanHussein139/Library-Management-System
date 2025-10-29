from fastapi import APIRouter, Depends, HTTPException, status,Query
from uuid import UUID
from typing import List
from typing import Optional

from app.application.services.member_service import MemberService
from app.interfaces.http.dependencies import get_member_service
from app.application.dto.member_dto import (
    MemberCreate,
    MemberUpdate,
    MemberResponse,
)

router = APIRouter()

@router.post("/", response_model=MemberResponse, status_code=status.HTTP_201_CREATED)
def create_member(dto: MemberCreate, service: MemberService = Depends(get_member_service)):
    try:
        return service.create_member(dto.name, dto.email)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=list[MemberResponse])
def get_all_members(
    skip: int = 0,
    limit: int = 10,
    search: Optional[str] = Query(None, description="Search by name or email"),
    service: MemberService = Depends(get_member_service),
):
    return service.get_all_members(skip=skip, limit=limit, search=search)



@router.get("/{member_id}", response_model=MemberResponse)
def get_member_by_id(member_id: UUID, service: MemberService = Depends(get_member_service)):
    member = service.get_member_by_id(member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    return member


@router.put("/{member_id}", response_model=MemberResponse)
def update_member(
    member_id: UUID,
    dto: MemberUpdate,
    service: MemberService = Depends(get_member_service),
):
    updated = service.update_member(member_id, dto)
    if not updated:
        raise HTTPException(status_code=404, detail="Member not found")
    return updated


@router.delete("/{member_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_member(member_id: UUID, service: MemberService = Depends(get_member_service)):
    deleted = service.delete_member(member_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Member not found")
    return
