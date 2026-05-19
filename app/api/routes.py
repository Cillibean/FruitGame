from fastapi import APIRouter
from app.db.session import get_db

router = APIRouter()

@router.get("/hello")
async def hello():
    return {"message": "Hello, World!"}