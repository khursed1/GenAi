from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

load_dotenv()
llm = ChatOpenAI()


class Movie(BaseModel):
    title: str
    genre: str
    rating: float


parser = PydanticOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_template("""Give information about the movie {title}
{format_instructions}
""")

prompt = prompt.partial(format_instructions=parser.get_format_instructions) 

chain=prompt|llm|parser

result=chain.invoke({'title':'inception'})

print(result)
print(type(result))