from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()
# Chatprompttrmplate takes input as list of tupple
template = ChatPromptTemplate(
    [
        ("system", "you are an exprienced software developper"),
        ("human", "explain how would solve this problem: {problem} step by steps")
    ]
)
prompt = template.invoke({"problem": "i want to earn money fast while learing skills"})
result = model.invoke(prompt)

print(result.content)
