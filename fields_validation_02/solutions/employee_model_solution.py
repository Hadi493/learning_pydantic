from pydantic import BaseModel, Field # type: ignore
from typing import Optional

# TODO: Create employee model
# Fields:
# - id: int
# - name: str (min 3 chars)
# - department: Optional str (default 'general')
# - salary: float (must be >= 10000)


class Employee(BaseModel):
    id: int
    name: str = Field(..., min_length=3)
    department: Optional[str] = 'General'
    salary: float = Field(..., ge=10000)
