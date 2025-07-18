from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class MemoryItem(BaseModel):
    id: int
    content: str

@router.get("/", response_model=List[MemoryItem])
def list_memory():
    return [] 