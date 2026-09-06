from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import ToolMessage

## So Far
# User → LLM → Answer

# With tools

# User
#  ↓
# LLM
#  ↓
# "I should use multiply"
#  ↓
# Tool
#  ↓
# 200
#  ↓
# LLM
#  ↓
# Final answer

#### NOTE- The llm does not execute the tool itself, it request to run the tool, your application
### execute the tool.


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


@tool
def add(a: int, b: int) -> int:
    """Add a and b."""
    return a + b


load_dotenv()
llm = ChatOpenAI()

llm_with_tool = llm.bind_tools([multiply, add])  # Bind tools takes list as input

response = llm_with_tool.invoke("What is 10*30")
print(response.tool_calls)

tools = {"multiply": multiply, "add": add}

tool_name = response.tool_calls[0]['name']
tool_argsA = response.tool_calls[0]["args"]["a"]
tool_argsB = response.tool_calls[0]["args"]["b"]

tool = tools[tool_name]
result = tool.invoke({"a": tool_argsA, "b": tool_argsB})

print(result)
