from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
llm = ChatOpenAI()

prompt = PromptTemplate.from_template("Explain about {topic}.")
parser = StrOutputParser()


def uppercase(data):
    # Note in lcel the input is dictionary so we use
    data["topic"] = data["topic"].upper()
    return data


runnable_uppercase = RunnableLambda(uppercase)
chain = runnable_uppercase | prompt | llm | parser

result=chain.invoke({'topic':'litracy'})
print(result)
