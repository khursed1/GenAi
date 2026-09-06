from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm=ChatOpenAI()
parser=JsonOutputParser()

prompt=PromptTemplate.from_template(
    """Give info about {topic}'
    Return answer in json format
    with these fields
    -name
    -age
    -country
    """
)

chain=prompt|llm|parser

# Suppose the l""""""lm returns
"""
{
    "name": "Python",
    "type": "Programming Language",
    "difficulty": "Beginner"
}
"""

# The parser converts automatically into python dictionary
result=chain.invoke({'Indian Prime Minister'})
print(result)