from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.runnables import RunnableLambda, RunnableBranch
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
llm = ChatOpenAI()

simple_prompt = PromptTemplate.from_template("Expalin about {topic} in simple language")
advance_prompt = PromptTemplate.from_template(
    "Explain about {topic} in techincal terms"
)

simple_chain = simple_prompt | llm | StrOutputParser()
advance_chain = advance_prompt | llm | StrOutputParser()

branch = RunnableBranch(
    (
        lambda x: x["level"] == "advance",
        simple_chain,
    ),
    advance_chain,
)

result=branch.invoke({'level':'simple','topic':'Ai'})
print(result)