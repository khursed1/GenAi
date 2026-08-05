# Pydantic is data validation and data parsing library in python.
# Using it we can make date structured, type-safe(matlab string bola to string hi aana chahiye)
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Optional

load_dotenv()
model = ChatOpenAI()


class Student(BaseModel):
    name: str
    age: Optional[int] = None


class Student2(BaseModel):
    name: list[str]


new_student = {"name": "alam"}
student1 = {"name": "alam", "age": "20"}
student = Student(**new_student)  # ** unpacks the dictionary and pass as key value pair
print(student)
student2 = Student(**student1)
print(student2)

structured_model = model.with_structured_output(
    Student2
)  # with structured output tells that i want op
# like class Student2
result = structured_model.invoke(
    "Ram Shayam and kavya study in gnit i want to extract their names"
)
print(result)
