from langchain_core.prompts import ChatPromptTemplate
chat_template=ChatPromptTemplate([
    ('system','you are a helpful {domain} expert'),
    ('human','Explain about the {topic}')
])

prompt=chat_template.invoke({'domain':'cricket','topic':'lbw'})

print(prompt)