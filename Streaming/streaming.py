from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
llm = ChatOpenAI()

prompt = PromptTemplate.from_template("Explain {topic} in simple language")

chain = prompt | llm | StrOutputParser()

# Normally we do chain.invoke() and we get result after the model has completely given output
# But using stream we get result piece by piece as the model generates it
for chunk in chain.stream({"topic": "mcp"}):
    print(chunk, end="", flush=True)
