# System prompt

### System prompt is instruction from the developper to the llm, like how to behave and what to do etc

### Eg

```text
You are a math assistant.
Use tools whenever calculations are required.
Do not perform calculations yourself.
```

# User prompt

## Its the actual request made by the user. 
```text
Whars 23 * 5
```

## So

```text
SYSTEM
  ↓
How should the agent behave?

USER
  ↓
What does the user want?
```

### NOTE- System prompt always do not gurantee the behabviour, sometimes agent can behave unexpectively so in production apps we use multi layer of validation guardrails etc.