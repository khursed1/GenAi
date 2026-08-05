from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

load_dotenv()

model=ChatOpenAI()
history=[SystemMessage(content="You are a helpful ai assistance which cracks jokes after answering the question")]
while True:
    user_input=input('User: ')
    history.append(HumanMessage(content=user_input))
    if user_input=='exit':
        break
    result = model.invoke(history)
    history.append(AIMessage(content=result.content))
    print("Ai: ",result.content)
