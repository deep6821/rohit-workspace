from typing import Optional
from pydantic import BaseModel


class Course(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    author: Optional[str] = None
