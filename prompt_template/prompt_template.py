from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()
llm = ChatOpenAI()
prompt_temp = PromptTemplate.from_template(
    "Explain about the {topic} in easy language in {words} words"
)
prompt = prompt_temp.invoke({"topic": "ai",'words':30})
result = llm.invoke(prompt)
print(result.content)
