from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from typing import TypedDict, Annotated, Optional

load_dotenv()
model = ChatOpenAI(model="gpt-4")


class Review(TypedDict):
    summary: str
    sentiment: str


# we can also send annotated string so that some llms get to know easily what is the meaning
class AReview(TypedDict):
    summary: Annotated[str, "summarize the given data"]
    sentiment: Annotated[str, "Also tell what is the sentiment positive or negative"]
    name: Annotated[Optional[str], "tell me the name of plant"]


structured_model = model.with_structured_output(AReview)
result = structured_model.invoke("""
The plant looked great and green but the stem was drying, and i think it wont survive, grapes plant was wrost
""")
print(result["summary"])
print(result["sentiment"])
print(result['name'])
