from turtle import title
from scalar_fastapi import get_scalar_api_reference
from fastapi import FastAPI


app = FastAPI()

@app.get("/scalar")
def get_scalar():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title   
    )
    
    



