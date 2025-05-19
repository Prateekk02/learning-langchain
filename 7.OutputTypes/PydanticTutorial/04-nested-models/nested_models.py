'''
Create a model
    - Each Course has modules
    - Each modules has lessons 
'''
from pydantic import BaseModel
from typing import Optional, List

class Address(BaseModel):
    street: str
    city: str
    postal_code: str
    
class User(BaseModel):
    id: int
    name: str
    address: Address
    
# Self referencing
class Comment(BaseModel):
    id: int 
    content: str
    replies: Optional[List['Comment']] = None  # This is forward referencing
    
Comment.model_rebuild()   # It rebuilds for forward referencing.

## Example

address = Address(
    street='221B Baker Street',
    city='London',
    postal_code="NW1 6XE"
)

user = User(
    id= 1,
    name= "Sherlock Holmes",
    address=address
)

comment = Comment(
    id= 1,
    content="When you have eliminated the impossible, whatever remains, however improbable, must be the truth.",
    replies=[
        Comment(id=2, content="Well said"),
        Comment(id=3, content="Yup!!!")
    ]
)