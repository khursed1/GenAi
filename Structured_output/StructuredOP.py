# Structured op means giving output in well defined data format like json dictionary etc
from typing import TypedDict

# typed disctionary tells what is the type of of the variable. It doesnot give error if we give
# wrong type
class Person(TypedDict):
    name: str
    age: int


new_person: Person = {"name": "khursed", "age": 23}
print(new_person)
