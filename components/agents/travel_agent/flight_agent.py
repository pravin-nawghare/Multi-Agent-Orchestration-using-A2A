from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage
from config import setting
from components.graph.state import AgentState
from components.tools.flight_tool import search_flights

flight_llm = setting.GEMINI_MODEL
secret_key = setting.GEMINI_API_KEY

if not secret_key:
    raise ValueError(f"Api key not provided")

flight_model = ChatGoogleGenerativeAI(
    model = flight_llm,
    api_key = secret_key
)

def flight_agent(state: AgentState) -> dict:
    query = state['user_query'].content
    # search for flights based on user travel destination
    response = search_flights(query=query)

    print(f"flight_agent: {response}\n")

    return {
        "flight_result": response,
        'messages': [
            AIMessage(content="Flight results fetched")
        ],
    }