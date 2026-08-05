from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage

load_dotenv()
model = ChatOpenAI()

template = ChatPromptTemplate(
    [
        ("system", "you are a helpful assistance"),
        MessagesPlaceholder("chat_history"),
        ("human", "{question}"),
    ]
)

chat_history = []  # Used for storing chat history

while True:
    user_input = input("you: ")
    if user_input == "exit":
        break

    if user_input == "history":
        print("------------------  CHAT HISTORY  --------------------")
        for messages in chat_history:
            if isinstance(messages,AIMessage):
                print("Ai: ", messages.content)
            else:
                print("You: ", messages.content)
    elif user_input == "clear":
        chat_history.clear()
    else:
        prompt = template.invoke({"question": user_input, "chat_history": chat_history})
        result = model.invoke(prompt)
        chat_history.append(HumanMessage(content=user_input))
        chat_history.append(AIMessage(content=result.content))
        print("Ai: ", result.content)
