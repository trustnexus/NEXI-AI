from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class CommandItem(BaseModel):
    id: int
    command: str

@router.get("/", response_model=List[CommandItem])
def list_commands():
    return [] 