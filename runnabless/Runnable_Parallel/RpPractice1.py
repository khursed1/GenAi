from langchain_core.runnables import RunnableParallel, RunnableLambda
from langchain_core.prompts import PromptTemplate

# creating three independent function
uppercase = RunnableLambda(lambda x: x.upper())
lowercase = RunnableLambda(lambda x: x.lower())
count = RunnableLambda(lambda x: len(x))

parallel=RunnableParallel(
    uppercase=uppercase,
    lowercase=lowercase,
    charcount=count
)

result=parallel.invoke('Hello')
print(result)
