from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
# HumanMessage is the message which a user send to the llm
# AiMessage is reply send back by llm
# SystemMessage is role assigned to the ai model
messages=[
    SystemMessage(content='you are a math teacher who answer in mathmatical tone'),
    HumanMessage(content='Tell me about milky way')
]

model=ChatOpenAI()
result=model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)