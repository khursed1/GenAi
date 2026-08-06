# Runnable Parallel

### Runnable parallel allows to run multiple runnable at the same time on same input

### Suppose you ask What is python?, Instead of  doing one task you want to find

* Summarize it
* Translate it into hindi
* Analyze its sentiment

### All these things can be done at a single time using runnable parallel

```text
               "Explain Python"

                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
    Summarizer   Translator   Sentiment
        │            │            │
        └────────────┼────────────┘
                     ▼
                 Final Result
```

### Why do we need it?

Without `RunnableParallel`

```python
summary=summary_chain.invoke(text)
translation=translation_chain.invoke(text)
sentiment=sentiment_chain.invoke(text)
```

With `RunnableParallel:`

```python
parallel=RunnableParallel(
    summary=summary_chain,
    translation=translation_chain,
    sentiment=sentiment_chain,

)
result=parallel.invoke(text)
```

#### The output of runnable parallel is dictionary
