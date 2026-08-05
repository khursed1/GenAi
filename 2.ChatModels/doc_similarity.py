from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
# initiliased enviroment evriable such as api key
load_dotenv()
embedding=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=300 )
document=['Virat kohli is known for his aggresive batting and leadership',
          'Ms dhoni is a former Indian Captain famous for his calm demeanor and batting skills',
          'Sachin Tendulkar, Also known as Master Blaster, holds many batting records',
          'Rohit Sharma is known for his elegant batting and record breaking double centuries',
          'Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers'
          ]
query='tell me about cricketer who is polite'
doc_embedding=embedding.embed_documents(document)
query_embedding=embedding.embed_query(query)
# cosine similarity takes 2d list
print(cosine_similarity([query_embedding],doc_embedding))
scores=cosine_similarity([query_embedding],doc_embedding)[0] # Cosine similarity gives answer as 2d list

# enumurate add index to each element, 
# then list convert enumerate object into list
# lambda x:x[1] is used to short based on the second element
index,score=sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]
print(document[index])