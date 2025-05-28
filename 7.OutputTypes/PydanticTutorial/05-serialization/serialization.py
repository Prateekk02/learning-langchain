from pydantic import BaseModel
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str
    
class User(BaseModel):
    id: int 
    name: str
    email: str
    is_active: bool = True
    address: Address
    createdAt: datetime
    tags: List[str] = []
    

# Creating a user instance

user = User(
    id= 1,
    name= "Sherlock Holmees",
    email= "sherlock.holmes329@gmail.com",
    createdAt= datetime(2024, 3, 15, 14, 30),
    address= Address(
        street= "Baker's Street",
        city= "London",
        zip_code= "NWX 316",
    ),
    tags= ['Detective', 'Chemist', 'Not so social']
)

# Using model_dump() -> dict
python_dict = user.model_dump()
print(type(python_dict))    

# Using model_dump_json() -> json
json_str = user.model_dump_json()
print(type(json_str))

