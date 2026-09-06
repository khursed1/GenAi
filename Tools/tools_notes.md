# Tools

## Tools are what allow an LLM to do things beyond simply generating text

## Until now, our flow has mostly been

``` Text
User
 ↓
Prompt
 ↓
LLM
 ↓
Answer

```

## But suppose the user ask whats the current temperature of my city

```text
User
 ↓
LLM
 ↓
I need the weather api
 ↓
Weather api Tool
 ↓
Result
 ↓
LLM
 ↓
Final answer
```

## A tool is a simple function that llm can use

### EG: A normal python function can be converted into tool

```python
def sum(a,b):
    return a+b
```

### This simple python function can be converted into tool using `@tool` decorator

```python
from langchain_core.tools import tool
@tool
def sum(a:int,b:int)->int:
    """ Add two numbers"""
    return a+b

```

### Thats it, now llm knows tool name, what it does using the `docstring` provided as string

### The input type and output type

### Langchain automaticaly generates schema of the function and send it to the llm so the llm can understand exactly what is tool about.

