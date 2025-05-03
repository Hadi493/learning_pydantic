from pydantic import BaseModel
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
    replies: Optional([List('Comments')])  # :: Forword Reference


Comments.model_rebuild()
