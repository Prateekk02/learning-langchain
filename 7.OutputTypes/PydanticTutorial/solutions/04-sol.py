'''
    Create a model
        - Each Course has modules
        - Each modules has lessons 
'''

from pydantic import BaseModel
from typing import List, Optional


class Lesson(BaseModel):
    lesson_id: int
    topic: str

class Modules(BaseModel):
    module_id: int
    name: str
    lesson: List[Lesson]
    
class Course(BaseModel):
    course_id: int 
    name: str
    module: List['Modules']
    