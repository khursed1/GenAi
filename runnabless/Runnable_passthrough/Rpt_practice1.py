from langchain_core.runnables import RunnablePassthrough

passthrough=RunnablePassthrough()

chain=RunnablePassthrough.assign(
    uppercase=lambda x:x['question'].upper()
)
result=chain.invoke({'question':'what is python?'})
print(result)