from langchain_core.runnables import RunnableParallel, RunnableLambda
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
llm = ChatOpenAI()

# Lets create
uppercase = RunnableLambda(lambda x: x.upper())
length = RunnableLambda(lambda x: len(x))

# lets combine them
parallel = RunnableParallel(
    uppercase=uppercase,
    length=length,
)
result = parallel.invoke("python")  # here both function receive the same input
print(result)

# using it with llm
Summmary = PromptTemplate.from_template("Give short summary about {person} life")
Learnings = PromptTemplate.from_template("Give key learning abour {person} life")

summary_chain = Summmary | llm | StrOutputParser()
learning_chain = Learnings | llm | StrOutputParser()

parallel = RunnableParallel(
    summary=summary_chain,
    learning=learning_chain,
)

result=parallel.invoke({'person':'Apj abdul kalam'})
print(result['summary'])
print(result['learning'])
