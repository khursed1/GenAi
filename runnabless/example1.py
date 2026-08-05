from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
llm = ChatOpenAI()

prompt = PromptTemplate.from_template("Explain about {topic} in {words} words")
parser = StrOutputParser()
chain = prompt | llm | parser
response = chain.invoke({"topic": "india", "words": 30})
print(response)
