from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_core.example_selectors import SemanticSimilarityExampleSelector

from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

load_dotenv()
llm = ChatOpenAI()

examples = [
    {
        "question": "what is python",
        "answer": "python is a programming language",
    },
    {
        "question": "What is HTML?",
        "answer": "Markup language",
    },
    {
        "question": "What is CSS?",
        "answer": "Styling language",
    },
    {
        "question": "What is SQL?",
        "answer": "Database language",
    },
]

example_prompt = PromptTemplate.from_template("Question: {question}\nAnswer: {answer}")

selector = SemanticSimilarityExampleSelector.from_examples(
    examples,  # this is example of index
    OpenAIEmbeddings(),  # this convert each example into embeddings
    Chroma,  # it store the embeddings and perform similarity search
    k=2,  # return two most similar examples
)

few_sot_prompt = FewShotPromptTemplate(
    example_selector=selector,  # example selected
    example_prompt=example_prompt,
    suffix="Question:{question}\nAnswer:",
    input_variables=["question"],
)

chain = few_sot_prompt | llm
response = chain.invoke({"question": "what is javascript"})
print(response.content)
