from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()
llm = ChatOpenAI()

prompt_temlate = PromptTemplate.from_template("write a short biography of {person}")
chain=prompt_temlate|llm

result=chain.invoke({'person':'APJ abdul kalam'})
print(result.content)