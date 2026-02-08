from datetime import date
from sqlmodel import SQLModel, Field
from uuid import UUID

class TodoResponse(SQLModel):
    id: UUID
    title: str
    desc: str | None = None
    deadline: date
    
class TodoRequest(SQLModel):
    title: str = Field(max_length=255, min_length=1)
    desc: str | None = Field(default=None, max_length=1000)
    deadline: date 