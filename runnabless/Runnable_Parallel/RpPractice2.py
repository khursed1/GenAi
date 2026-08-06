from langchain_core.runnables import RunnableParallel
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
llm = ChatOpenAI()

explain_consise = PromptTemplate.from_template("Explain about {topic} in one sentence")
explain_detail = PromptTemplate.from_template("Explain about {topic} in 50 words")
explain_kid = PromptTemplate.from_template("Explain about {topic} to a kid")

consise_chain = explain_consise | llm | StrOutputParser()
detailed_chain = explain_detail | llm | StrOutputParser()
kid_chain = explain_kid | llm | StrOutputParser()

parallel = RunnableParallel(
    consize=consise_chain,
    detailed=detailed_chain,
    kid=kid_chain,
)

result=parallel.invoke({'topic':'programming'})

print(result['consize'])
print(result['detailed'])
print(result['kid'])

