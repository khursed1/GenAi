from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

load_dotenv()
llm = ChatOpenAI()

prompt = PromptTemplate.from_template("Explain about {topic}")
parser = StrOutputParser()


def countChar(data):
    count = 0
    stri = data
    for ch in stri:
        if ch != " ":
            count += 1
    return count


chain = prompt | llm | parser | RunnableLambda(countChar)

result = chain.invoke({"topic": "abacus"})
print('No of chars is ',result)
