from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

loader=TextLoader('../company.txt') # Loading external text file
documents=loader.load() # loading and converting the text file into document object


load_dotenv()
# creating embedding object
embedding = OpenAIEmbeddings(model="text-embedding-3-small")
llm=ChatOpenAI()
# lets create our vector store
vector_store = Chroma(
    # Name of the storage
    collection_name="my_document",
    embedding_function=embedding,
)

# Lets setup our retriever
retriever = vector_store.as_retriever(search_kwargs={"k": 1})

prompt = ChatPromptTemplate.from_template("""
Answer the question using only the following context.
Context:{context}
Question:{question}
""")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=10,
)

chunks=splitter.split_documents(documents)

vector_store.add_documents(chunks) # Add chunks into the vector store
question="What does this company create"
doc=retriever.invoke(question)
context="\n\n".join(
   d.page_content for d in doc
)
result=prompt.invoke({"context":context,"question":question})

response=llm.invoke(result)
print(response.content)