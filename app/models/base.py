# app/models/base.py
from sqlmodel import SQLModel


__all__ =["SQLModel","metadata"]

class BaseModel(SQLModel):
    pass
