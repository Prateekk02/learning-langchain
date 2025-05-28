'''
The datetime in serialization.py in model_dump_json() was in weired format :XD,
therefore, CofigDict from Pydantic is used 
'''

from pydantic import BaseModel, ConfigDict
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
    
    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y  %H:%M:%S')}
    )
    

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
print(python_dict)    


print("=" * 50)
# Using model_dump_json() -> json
json_str = user.model_dump_json()
print(json_str)

 