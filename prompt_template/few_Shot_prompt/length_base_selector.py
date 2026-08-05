from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_core.example_selectors import LengthBasedExampleSelector

load_dotenv()
llm = ChatOpenAI()

examples = [
    {"question": "What is Python?", "answer": "Programming language"},
    {"question": "What is Java?", "answer": "Programming language"},
    {"question": "What is SQL?", "answer": "Database language"},
    {"question": "What is HTML?", "answer": "Markup language"},
]
example_prompt = PromptTemplate.from_template("question: {question}\nanswer: {answer}")

selector = LengthBasedExampleSelector(
    examples=examples, example_prompt=example_prompt, max_length=80
    # max length means the length of the text not no of examples
)

few_shot_prompt = FewShotPromptTemplate(
    example_selector=selector,
    example_prompt=example_prompt,
    suffix="Question: {question}\nAnswer: ",
    input_variables=["question"],
)
chain = few_shot_prompt | llm

response = chain.invoke({"question": "what is css"})
print(response.content)
