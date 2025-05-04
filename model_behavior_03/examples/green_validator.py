from pydantic import BaseModel, field_validator, model_validator, computed_field # type: ignore


class User(BaseModel):
    username: str  # Fixed typo in field name

    @field_validator('username')
    def username_legnth(cls, v):
        if len(v) < 4:
            raise ValueError("Username must be at least 4 characters")
        return v


class SignupData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')  # Fixed by adding quotes around 'after'
    def password_match(cls, values):
        if values.password != values.confirm_password:  # Fixed incorrect attribute reference
            raise ValueError("Passwords do not match")  # Fixed typo in error message
        return values


class Product(BaseModel):
    price: int
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
