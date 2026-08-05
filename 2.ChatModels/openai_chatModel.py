from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model='gpt-4')
result=model.invoke("who is health minister of bihar and what is his relation with nitish")

print(result.content)