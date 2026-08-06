from langchain_core.runnables import RunnablePassthrough

# create object of passthrough
passthrough = RunnablePassthrough()

result = passthrough.invoke("Hello")

print(result) # OP: Hello (Unchanged)
result2=passthrough.invoke({
    'name':'khursed',
    'age':23
})

print(result2)
