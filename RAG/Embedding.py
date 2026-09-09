from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-small")

vector_store = Chroma(
    collection_name="my_document",
    embedding_function=embedding,
)

text = """
Python is a high-level programming language.
It was created by Guido van Rossum.

Python is widely used in artificial intelligence,
data science, web development, and automation.

Python has a large ecosystem of libraries.
"""
splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=10,
)

chunks = splitter.create_documents([text])

vector_store.add_documents(chunks)

result = vector_store.similarity_search(
    "who created python",
    k=1,
)

print(result)
