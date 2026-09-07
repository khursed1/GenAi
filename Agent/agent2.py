from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from langchain_core.tools import tool

load_dotenv()
llm=ChatOpenAI()

@tool
def add(a:int,b:int)->int:
    """Add two numbers"""
    return a+b
@tool
def subtract(a:int,b:int)->int:
    """Subtract b from a """
    return a-b



agent=create_agent(
    model=llm,
    tools=[add,subtract],
    system_prompt="You are a helpful math teacher. Use the provided tools for calculation"
)