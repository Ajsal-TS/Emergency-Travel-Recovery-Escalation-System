
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
import uuid

class Alert(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str
    description: str
    status: str = Field(default="new")  # new, acknowledged, escalated, resolved
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None

    histories: List["AlertHistory"] = Relationship(back_populates="alert")
    assignments: List["Assignment"] = Relationship(back_populates="alert")

class AlertHistory(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    alert_id: uuid.UUID = Field(foreign_key="alert.id")
    status: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    alert: Alert = Relationship(back_populates="histories")

class Assignment(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    alert_id: uuid.UUID = Field(foreign_key="alert.id")
    user_id: uuid.UUID = Field(foreign_key="user.id")
    shift_id: Optional[int] = Field(foreign_key="shift.id", default=None)

    alert: Alert = Relationship(back_populates="assignments")
