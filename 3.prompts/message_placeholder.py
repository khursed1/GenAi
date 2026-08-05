from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

# Message placeholder is used to dynamically insert text into the chat prompt template
chat_history = [
    HumanMessage(content="Hi"),
    AIMessage(content="Hello!"),
    HumanMessage(content="What is Python?"),
]

prompt = ChatPromptTemplate(
    MessagesPlaceholder(variable_name='chat_history'),
    ("system", "you are a helpful {role}"),
    ("human", "explain about {topic}"),
)


prompt.invoke(
    {
        "role": "Math teacher",
        "topic": "Fun facts about circle",
        "chat_history": chat_history,
    }
)

print(prompt)
