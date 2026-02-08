from datetime import date
from pydantic import BaseModel

class TodoResponse(BaseModel):
    title: str | None = None
    desc: str | None = None
    deadline : date | None = None 
    
class TodoRequest(BaseModel):
    id: str
    title: str | None = None
    desc: str | None = None
    deadline: date | None = None