from langchain_core.prompts import PromptTemplate

extraction_prompt = PromptTemplate(
    input_types= [
        "user_query"
    ],
    template="""
    Extract only destination city or country from given query.
    Do not extract origin city or country or any other data.

    Query:
    {user_query}

    Return only destination name
"""
)

