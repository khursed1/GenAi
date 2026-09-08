# RAG
Suppose you give an AI a 300-page PDF and ask:

"What is the company's revenue in 2025?"

The LLM doesn't automatically know what's inside your PDF.

RAG solves this by giving the LLM relevant information from your documents at the time of the question.

The basic flow is:

```text
                 YOUR DOCUMENT
                       ↓
                  Split into chunks
                       ↓
                   Embeddings
                       ↓
                  Vector Database
                       ↓
User question → Embedding → Search
                              ↓
                       Relevant chunks
                              ↓
                             LLM
                              ↓
                           Answer
```

### RAG helps to perform semantic based search.

## It has two major phases.

### Phase 1 -Indexing

#### We prepare our document befor user ask anything.

```text
PDF
 ↓
Load
 ↓
Split
 ↓
Convert into Embeddings
 ↓
Store in vector DB
```

### Phase 2- Retrieval + Generation

#### When a user ask question.

```text
Question
 ↓
Embed question
 ↓
Search vector DB
 ↓
Retrieve relevant chunks
 ↓
Give chunks + question to LLM
 ↓
Answer
```

### So:

```text
          INDEXING
             ↓
       Vector Database
             ↓
        ─────────────
             ↓
         RETRIEVAL
             ↓
        Relevant data
             ↓
        GENERATION
             ↓
           Answer
```


### ⭐ The RAG formula

```text
RAG = Retrieval + Generation
```

```text
Retrieve relevant information
             +
Give it to the LLM
             =
Grounded answer
```
