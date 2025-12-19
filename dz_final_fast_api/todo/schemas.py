from pydantic import BaseModel
from typing import Optional

class ItemCreate(BaseModel):
    title: str
    description: Optional[str] = ""
    completed: bool = False

class ItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None