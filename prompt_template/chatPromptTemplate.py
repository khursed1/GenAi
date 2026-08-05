from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
llm = ChatOpenAI()

template = ChatPromptTemplate.from_messages(
    [
        ("system", "you are an exprienced {position}"),
        ("human", "Explain about {topic} in {words} words"),
    ]
)

chain = template | llm
result = chain.invoke({"position": "doctor", "topic": "fever", "words": 30})
print(result.content)
