from sqlmodel import select
from fastapi import APIRouter, status, Depends
from app.utils.standard_query_param import standard_query_param
from app.models.engine import get_db
from app.models.database import Todo
from app.schema.todo import TodoRequest, TodoResponse
todo_router = APIRouter(
    tags=   ["Todo"]
)

@todo_router.get("/todo", response_model=list[TodoResponse])
def get_todo(param = Depends(standard_query_param), 
             db =  Depends(get_db)):
    stmt = select(Todo)
    stmt = stmt.limit(param["limit"])
    todos = db.exec(stmt).all()
    
    return todos


@todo_router.post("/todo", status_code=status.HTTP_201_CREATED, response_model=TodoResponse)
def create_todo(todo: TodoRequest,
                db = Depends(get_db)
):
    db_todo = Todo(**todo.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo