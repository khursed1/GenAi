from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_chroma import Chroma
from langchain_core.example_selectors import SemanticSimilarityExampleSelector

load_dotenv()
llm = ChatOpenAI()

examples = [
    {"movie": "Inception", "genre": "Sci-Fi"},
    {"movie": "The Conjuring", "genre": "Horror"},
    {"movie": "Finding Nemo", "genre": "Animation"},
    {"movie": "Titanic", "genre": "Romance"},
]

example_prompt = PromptTemplate.from_template("Movie: {movie}\nGenre:{genre}")
# here we are using semantic selector to retrieve results with similarities
selector = SemanticSimilarityExampleSelector.from_examples(
    examples,
    # Examples ko embedding me convert karo
    OpenAIEmbeddings(),
    # chroma me store karo
    Chroma,
    # most 2 relevant result ko return karo
    k=1,
)

few_sot_prompt = FewShotPromptTemplate(
    example_selector=selector,
    example_prompt=example_prompt,
    suffix="Movie:{movie}\nGenre:",
    input_variables=["movie"],
)
prompt=few_sot_prompt.invoke({'movie':'bhootnath'})
print(prompt.text)
# chain = few_sot_prompt | llm

# response = chain.invoke({"movie":"fifty shades of grey"})
# print(response.content)
