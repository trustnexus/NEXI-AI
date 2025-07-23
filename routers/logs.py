from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class LogItem(BaseModel):
    id: int
    message: str

@router.get("/", response_model=List[LogItem])
def list_logs():
    return [] 