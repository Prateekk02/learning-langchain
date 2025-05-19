'''
Create a Booking Model
Fields: 
    - user_id : int
    - room_id : int
    - nights : int (must be >=1)
    - rate_per_night : float 
    - Also add computed_field: total_amount = nights * rate_per_night 
'''

from pydantic import BaseModel, Field, computed_field

class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., gt=1)
    rate_per_night: float
    
    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.rate_per_night
     