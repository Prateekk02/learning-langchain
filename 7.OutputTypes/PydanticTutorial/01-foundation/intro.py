from pydantic import BaseModel
class User(BaseModel):
    id : int
    name : str
    is_active : bool  

input_data = {'id': 1, 'name': 'Anakin', 'is_active': True}  # Won't throw an error
# input_data = {'id' : '1', 'name' : 'Anakin', 'is_active' : 'True'}   # This will also not throw error as it will convert '1' -> 1 and 'True' -> True
# input_data = {'id' : 1, 'name' : 'Anakin', isActive : True}   # This will  throw error as isActive cannot be converted to is_active.
user = User(**input_data)
print(user)