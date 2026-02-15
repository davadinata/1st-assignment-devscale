from scalar_fastapi import get_scalar_api_reference
from fastapi import FastAPI
from app.router.todo import todo_router


app = FastAPI()

app.include_router(todo_router)

@app.get("/")
def home():
    return {"message":"Welcome to todo apps"}

@app.get("/scalar")
def get_scalar():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title   
    )
    
    



