from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from config import setting
from components.prompts.final_response_prompt import response_prompt
from components.graph.state import AgentState

response_llm = setting.GEMINI_MODEL
secret_key = setting.GEMINI_API_KEY

if not secret_key:
    raise ValueError(f"Api key not provided")

response_model = ChatGoogleGenerativeAI(
    model = response_llm,
    api_key = secret_key
)

def final_response(state: AgentState):
    prompt = response_prompt.format(
        user_query = state.get("user_query", ""),
        travellers = state.get("travellers", ""),
        flight_result = state.get("flight_result", ""),
        hotel_result = state.get("hotel_result", ""),
        itineary_result = state.get("itineary_result", ""),
        weather_result = state.get("weather_result", "")
    )

    response = response_model.invoke([
        SystemMessage(content="You are a professional AI travel booking assistant"),
        HumanMessage(content=prompt)
    ])

    # print(f"final_response_agent response added in messages: {response}")

    return {
        'messages': [response],
    }