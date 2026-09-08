from langchain_core.documents import Document


doc=Document(
    page_content='Python was created by Guido van Rossum',
    metadata={'source':'python_history.txt'}
)

print(doc)
print(doc.page_content)
print(doc.metadata)