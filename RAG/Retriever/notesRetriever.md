# Retriever

### A retriever is a search interface of knowledge base.

```text
Question
   ↓
Retriever
   ↓
Relevant Documents
```
### How to create one

```python
retriever=vector_store.retriever(
    search_kwargs={"k":2}
)
```
### Then

```python
result=retriever.invoke("Who created python")
for doc in result:
    print(doc.page_content)
```
### The retiriever returns list of document object