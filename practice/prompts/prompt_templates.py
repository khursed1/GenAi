from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

template = PromptTemplate(
    template="Write a {tone} email about {subject} in {words} words.",
    input_variables=["tone", "subject", "words"],
)

prompt = template.invoke(
    {"tone": "professional", "subject": "internship application", "words": 120}
)
result = model.invoke(prompt)
print(result.content)
