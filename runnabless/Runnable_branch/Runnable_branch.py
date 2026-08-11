from langchain_core.runnables import RunnableBranch, RunnableLambda

branch = RunnableBranch(
    (lambda x: x >= 90, RunnableLambda(lambda x: "Excellent")),
    (lambda x: x >= 75,RunnableLambda(lambda x: "Very Good")),
    RunnableLambda(lambda x:'Needs Improvement')
)
print(branch.invoke(85))
