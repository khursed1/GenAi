from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
model = ChatOpenAI()

template = ChatPromptTemplate(
    [
        ("system", "you are an {expert}"),
        ("human", "explain about {topic} in less than 30 words"),
    ]
)
chain = template | model
result = chain.invoke({"expert": "doctor", "topic": "fever"})
print(type(result))
print(result.content)
