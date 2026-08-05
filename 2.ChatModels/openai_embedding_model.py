from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-small',dimensions=32)
# embed query is used to embed single query
result=embedding.embed_query('What is capital of india')

# for list of query we can use embed document 
document=['this is line 1',
          'this is line 2',
          'who is nehru']

result2=embedding.embed_documents(document)
print(result2)


