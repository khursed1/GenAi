from pydantic import BaseModel,Field
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Optional

load_dotenv()
model = ChatOpenAI()


class Student(BaseModel):
    name: str
    age: int
    stream: str
    marks: Optional[int] = None
strLLm=model.with_structured_output(Student)

op=strLLm.invoke('My name is khursed alam, and i am 20 years old i study in cse')
print(op)

# we use field with withstrop to give better instruction to the llm
class Car(BaseModel):
    name:str=Field(description='This represent the brand of the car')
    