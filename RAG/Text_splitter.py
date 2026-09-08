from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Python is a high-level programming language.
It was created by Guido van Rossum.

Python is widely used in artificial intelligence,
data science, web development, and automation.

Python has a large ecosystem of libraries.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
)

chunks=splitter.split_text(text)
for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i+1} ---")
    print(chunk)
