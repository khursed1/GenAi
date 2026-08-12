from langchain_core.runnables import RunnableAssign, RunnableLambda

data = {
    "name": "Khurshed",
    "age": 23,
    "city": "Patna",
}

assign = RunnableAssign(
    {
        "Adult": RunnableLambda(lambda x: x["age"] > 18),
        "upper_name": RunnableLambda(lambda x: x["name"].upper()),
    }
)

result = assign.invoke(data)  # it returns the original dictionary after assigning

print(result)
