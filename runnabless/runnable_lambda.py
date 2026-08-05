from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()
llm=ChatOpenAI()

def uppercase(text):
    return text.upper()

# converting above function into runnable
runnable_uppercase=RunnableLambda(uppercase)

print(runnable_uppercase.invoke('hIi'))