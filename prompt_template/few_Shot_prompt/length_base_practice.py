from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_core.example_selectors import LengthBasedExampleSelector

examples = [
    {"question": "What is Python?", "answer": "Programming language"},
    {"question": "What is Java?", "answer": "Programming language"},
    {"question": "What is SQL?", "answer": "Database language"},
    {"question": "What is HTML?", "answer": "Markup language"},
]

example_prompt = PromptTemplate.from_template("Question: {question}\nAnswer: {answer}")
selector = LengthBasedExampleSelector(
    examples=examples, example_prompt=example_prompt, max_length=10 
)

few_sot_prompt = FewShotPromptTemplate(
    example_selector=selector,
    example_prompt=example_prompt,
    suffix="Question: {question}\nAnswer:",
    input_variables=["question"],
)
formatted_prompt = few_sot_prompt.invoke({"question": "what is css"})
print(formatted_prompt.text)
