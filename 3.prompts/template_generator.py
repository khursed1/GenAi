from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["paper_input", "style_input", "length_input"],
    template="""
Please summarize the research paper titled "{paper_input}".

Requirements:

- Explanation Style: {style_input}
- Explanation Length: {length_input}

Mathematical Details:
- Include relevant mathematical equations if they are present in the paper.
- Explain mathematical concepts using simple and intuitive examples or code snippets where appropriate.

Analogies:
- Use relatable analogies to simplify complex ideas.

If any requested information is not available in the paper, respond with:
"Insufficient information available"

Do not guess or make up information.

Ensure the summary is clear, accurate, and follows the requested explanation style and length.
"""
)


template.save('template.json')