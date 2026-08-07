# Runnable Branch

## Runnable branch in `LCEL` is equivalent to `if else` in python

### In python

```python
if score >= 50:
    print("Pass")
else:
    print("Fail")
```

### In LCEL

```text
           Input
             │
     Condition True?
        /         \
      Yes         No
      │            │
 Runnable A   Runnable B
```

### Why do we need `Runnable Branch`

#### Suppose we are building bilingual chatbot

#### If user ask in hindi then we use HINDI prompt, if the user ask in English then we use English prompt
