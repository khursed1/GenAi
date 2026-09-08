# Why does document object exist

### Because RAG dont simply need text. It need details about the document like

```text
Document
├── page_content → actual text
└── metadata     → information about where it came from
```
### EG

```python
metadata={
    "source": "employee_handbook.pdf",
    "page": 17
}
```
# Document loader

### In real RAG application we do not manually write:
```python
Document(page_content="...")
```
### Instead we give our application something like `Report.pdf`.
### And langchain turn this pdf into document object, So we need document loaders.

```text
PDF / TXT / CSV / Web page
          ↓
    Document Loader
          ↓
    Document objects
          ↓
      RAG pipeline
```

### Diffrent file type has diffrent type of document loader.

```text
PDF       → PDF loader
TXT       → Text loader
CSV       → CSV loader
Web page  → Web loader
```

