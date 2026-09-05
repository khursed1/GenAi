# Streaming

## Until now, when you call

```python
result = chain.invoke(...)
```
## If the model takes 5 second to generate the response then we see output after 5 seconds
## But with streaming we get response as the model generate it
## Streaming means we get message piece by piece as the model generates it.

## Instead of 
```Text
Wait...
Wait...
Wait...

"Python is a programming language..."
```

## We get result as
```Text
Python
Python is
Python is a
Python is a programming
Python is a programming language
...
```