from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from config import setting
from components.graph.state import AgentState
from components.prompts.itineary_prompt import itineary_agent_prompt


itineary_llm = setting.GEMINI_MODEL
secret_key = setting.GEMINI_API_KEY

if not secret_key:
    raise ValueError(f"Api key not provided")

itineary_model = ChatGoogleGenerativeAI(
    model = itineary_llm,
    api_key = secret_key
)

def itineary_agent(state: AgentState) -> dict:
    itineary_prompt = itineary_agent_prompt.format(
        user_query = state.get("user_query", ""),
        travellers = state.get("travellers", ""),
        flight_result = state.get("flight_result", ""),
        weather_result = state.get("weather_result", ""),
        hotel_result = state.get("hotel_result", "")
    )

    response = itineary_model.invoke([
        SystemMessage(content="You are an expert travel planner"),
        HumanMessage(content=itineary_prompt)
    ])

    return {
        'messages': [response], # we using reducer so messages need to be added as list
        'itineary_result': response.content
    }