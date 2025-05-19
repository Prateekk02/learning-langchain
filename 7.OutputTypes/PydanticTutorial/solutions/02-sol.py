'''
Create Employee Model
- Fields
    - id: int
    - name: str (min 3 characters)
    - department: optional str (default 'General')
    - salary: float (must be >= 10000)   
'''

from pydantic import BaseModel, Field
from typing import Optional

class Employee(BaseModel):
    id: int
    name: str = Field(..., min_length=3, description="Employee Name")
    department: Optional[str] = 'General'
    salary: float = Field(..., gt=10000)