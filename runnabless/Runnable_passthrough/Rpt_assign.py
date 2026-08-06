from langchain_core.runnables import RunnablePassthrough

passthrough = RunnablePassthrough()
# Suppose the input is {'name':'alam'} and we want to add extra field into it named class
# ... so we use .assign(), The original data is preserved and new key is added

# Example
chain = RunnablePassthrough.assign(
    length=lambda x: len(
        x["question"]
    )  # using lambda function to calculate the length of question
)
result = chain.invoke({"question": "what is python?"})
print(result)
# Op: {'question': 'what is python?', 'length': 15}

result=chain.invoke({'question':'hii'})
print(result)