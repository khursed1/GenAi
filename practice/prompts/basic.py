from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()
Template = PromptTemplate(
    template="Explain about the {topic} in {words} words",
    input_variables=["topic", "words"],
)
prompt = Template.invoke({"topic": "python", "words": 20})
print(prompt)
print(model.invoke(prompt).content)