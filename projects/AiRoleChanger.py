from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
model = ChatOpenAI()

template = ChatPromptTemplate(
    [
        ("system", "you are a {role}"),
        MessagesPlaceholder("chat_history"),
        ("human", " {query}"),
    ]
)

# run an infininte loop so that the chatbot keeps running

chat_history = []

chain = template | model | StrOutputParser()
role = " "
while True:
    if role == " ":
        role = input("Set role: ")
    user_input = input("You: ")
    if user_input == "exit":
        break
    if user_input == "chng_role":
        role = input("Enter the role: ")
    else:
        result = chain.invoke(
            {"role": role, "query": user_input, "chat_history": chat_history}
        )
        chat_history.append(HumanMessage(content=user_input))
        chat_history.append(AIMessage(content=result))
        print("Ai: ", result)
