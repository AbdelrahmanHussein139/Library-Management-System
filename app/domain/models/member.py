from uuid import UUID

class Member:
    def __init__(self, member_id: UUID, name: str, email: str):
        self.member_id = member_id
        self.name = name
        self.email = email
