from langchain_core.runnables import RunnableLambda, RunnableAssign

data = {
    "name": "alam",
    "age": 23,
}

assign = RunnableAssign({"adult": RunnableLambda(lambda x: x["age"] > 18)})

result = assign.invoke(data)
print(result)

# Adding multiple field
assign = RunnableAssign(
    {
        "adult": RunnableLambda(lambda x: x["age"] > 18),
        "name_upper": RunnableLambda(lambda x: x["name"].upper()),
    }
)
result = assign.invoke(data)

print(result)
