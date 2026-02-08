from datetime import date
from pydantic import BaseModel

class TodoResponse(BaseModel):
    title: str
    desc: str | None = None
    deadline : date 
    
class TodoRequest(BaseModel):
    id: str
    title: str
    desc: str | None = None
    deadline: date 