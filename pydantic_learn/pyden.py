from pydantic import BaseModel
from typing import Optional
class Student(BaseModel):
    name:str
    age:int

student=Student(
    name='khursed',
    age='22'
)
# If we give wrong data type then it throws error
# s2=Student(
#     name='khursed',
#     age='adfd'
# )

# data types 
class Student2(BaseModel):
    name:str
    age:int
    height:float
    passed:bool
# Optional field
class S3(BaseModel):
    name:str
    age:Optional[int]=None
# now this will not give error even if you do not give age

# default values
class Car(BaseModel):
    company:str
    color:str='white' # this is default value if we dont pass the value then it will populate with white
car=Car(company='Tyota')
car2=Car(company='tesla',color='metalic')
print(car)
print(car2)