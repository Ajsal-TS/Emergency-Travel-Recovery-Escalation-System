
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
import uuid

class UserRoleLink(SQLModel, table=True):
    user_id: uuid.UUID = Field(foreign_key="user.id", primary_key=True)
    role_id: int = Field(foreign_key="role.id", primary_key=True)

class Role(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    users: List["User"] = Relationship(back_populates="roles", link_model=UserRoleLink)

class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    email: str
    is_active: bool = True
    roles: List[Role] = Relationship(back_populates="users", link_model=UserRoleLink)
