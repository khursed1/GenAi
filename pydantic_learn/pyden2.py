# Nested model
from pydantic import BaseModel

class Address(BaseModel):
    vill:str
    pin:int
class Student(BaseModel):
    name:str
    address:Address # Here we are using the address class which created above
s1=Student(
    name='khursed',
    address={
        'vill':'Rampur',
        'pin':'841405'
    }
)
print(s1.name)
print(s1.address)

# convert to dictionary
s2=s1.model_dump()
print(s2)

# convert to json
print(s1.model_dump_json())
