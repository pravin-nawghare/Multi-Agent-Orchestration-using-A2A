from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage
from config import setting
from components.graph.state import AgentState
from components.tools.websearch_tool import web_search
import asyncio


hotel_llm = setting.GEMINI_MODEL
secret_key = setting.GEMINI_API_KEY

if not secret_key:
    raise ValueError(f"Api key not provided")

hotel_model = ChatGoogleGenerativeAI(
    model = hotel_llm,
    api_key = secret_key
)

def hotel_agent(state: AgentState) -> dict:
    query = f"Find best hotels for {state.get('user_query', "")}"
    result  = asyncio.run(web_search(query=query))

    return {
        "hotel_result": result,
        'messages': [
            AIMessage(content="Hotel information fetched")
        ]
    }