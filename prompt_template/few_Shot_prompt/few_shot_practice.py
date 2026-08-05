from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

load_dotenv()
llm = ChatOpenAI()

examples = [
    {"Email": "Meeting about project updates", "Subject": "Project Update Meeting"},
    {
        "Email": "Interview scheduled for Monday",
        "Subject": "Interview scchedule confirmation",
    },
]

example_prompt = PromptTemplate.from_template("Email: {Email}\nSubject: {Subject}")

few_shot_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Email: {email}\nSubject: ",
    input_variables=["email"],
)

chain = few_shot_template | llm
response = chain.invoke({"email": "letter for planned leave for travelling"})

print(response.content)
