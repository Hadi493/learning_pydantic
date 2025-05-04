from pydantic import BaseModel # type: ignore
from typing import List, Optional


class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    id: int
    name: str
    address: Address  # :: Nested Reference


class Comments(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comments']] = None  # :: Forward Reference


Comments.model_rebuild()
