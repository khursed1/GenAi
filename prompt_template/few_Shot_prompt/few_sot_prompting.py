# few shot prompting is a technique in which we give few examples to the llm before taking output
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate

load_dotenv()
llm = ChatOpenAI()
# Examples are stored as list of dictionaries
examples = [
    {"input": "pizza", "output": "unhealthy"},
    {"input": "museli", "output": "healthy"},
    {"input": "salad", "output": "healthy"},
]

example_prompt = PromptTemplate.from_template("input: {input}\nOutput: {output}")
few_sot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Input: {question}\nOutput:",
    input_variables=["question"],
)
chain = few_sot_prompt | llm

response = chain.invoke({"question": "apple"})
print(response.content)
