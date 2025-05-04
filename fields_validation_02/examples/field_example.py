from pydantic import BaseModel # type: ignore
from typing import List, Dict, Optional


class Card(BaseModel):
    use_id: int
    items: List[str]
    quantities: Dict[str, int]


class blogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None
