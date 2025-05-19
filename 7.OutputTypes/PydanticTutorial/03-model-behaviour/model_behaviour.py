from pydantic import BaseModel, field_validator, model_validator, computed_field

class User(BaseModel):
    username: str
    
    @field_validator("username")
    def username_validator(cls, value):
        if value < 4:
            raise ValueError("Username must be atleast 4 character long.")
        return value
    


class SignupData(BaseModel):
    password: str
    confirmed_password: str
    
    @model_validator(mode='after')
    def password_match(cls, values):
        if values.password != values.confirmed_password:
            raise ValueError("Password do not match")
        
        return values
            
        
class Product(BaseModel):
    price: float
    quantity: int
    
    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity