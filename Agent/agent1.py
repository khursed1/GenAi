from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from langchain.agents import create_agent

load_dotenv()
llm = ChatOpenAI()


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b


@tool
def add(a: int, b: int) -> int:
    "Add two numbers"
    return a + b


# Lets create our agent by giving model and tools list

agent = create_agent(
    model=llm,
    tools=[multiply, add],
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What is perimeter of rectangle with length 10 and width 5"}]}
)
# print(result)

# The agent will perform

        # User asks question
        #        ↓
        # LLM sees available tools
        #        ↓
        # LLM chooses multiply
        #       ↓
        # multiply(25, 8)
        #        ↓
        # Tool returns 200
        #        ↓
        # LLM sees 200
        #        ↓
        # Final response

# lets see what types of messages are sent to and fro by agent

# for message in result['messages']:
#     print('\n---')
#     print(type(message))
#     print(message)

for message in result["messages"]:
    print(type(message).__name__)
    print(message)
    print()