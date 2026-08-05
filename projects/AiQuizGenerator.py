from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import AIMessage,HumanMessage
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

load_dotenv()
model=ChatOpenAI()
