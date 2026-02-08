import uuid
from datetime import date
from sqlmodel import SQLModel, Field


class Todo(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str = Field(max_length=255, min_length=1)
    desc: str | None = Field(default=None, max_length=1000)
    deadline: date
   