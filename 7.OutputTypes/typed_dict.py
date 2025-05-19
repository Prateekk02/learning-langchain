from typing import TypedDict

class Person(TypedDict):
    name : str
    age : int

new_person : Person = {
    'name': "Anakin",
    'age': 66
}

print(new_person)