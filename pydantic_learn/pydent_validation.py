from pydantic import BaseModel, Field


class Votor(BaseModel):
    name: str
    age: int = Field(gt=18)
v1=Votor(name='khursed',age=8)
