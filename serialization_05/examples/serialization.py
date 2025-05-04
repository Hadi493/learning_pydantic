from pydantic import BaseModel, ConfigDict # type: ignore
from typing import List
from datetime import datetime
from logging import config


class Address(BaseModel):
    city: str
    street: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    address: Address
    created_at: datetime
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')
        }
    )
# Create a user instance
user = User(
    id=1,
    name="John Doe",
    email="john.doe@example.com",
    address=Address(city="New York", street="123 Main St", zip_code="10001"),
    created_at=datetime(2024, 1, 1, 1, 12, 40),
    is_active=True,
    tags=["admin", "user"]
)

# Using model_dump()
python_dict = user.model_dump()
print(python_dict)
print("===================================================")
# Using model_dump_json()
json_str = user.model_dump_json()
print(json_str)
