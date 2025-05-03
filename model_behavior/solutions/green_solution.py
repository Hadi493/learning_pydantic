from pydantic import BaseModel, Field, computed_field

# TODO: Create Booking model
# Fields:
# - user_id: int
# - room_id: int
# - nights: int (must be >= 1)
# - rate_per_night: int
# Also, add computed field: total_amount = nights * rate_per_night


class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)
    rate_per_night: int

    @computed_field
    @property
    def total_amount(self):
        return self.nights * self.rate_per_night
