from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from config import setting
from components.graph.state import AgentState
from components.tools.flight_tool import aviation_mcp
from components.prompts.flight_prompt import FLIGHT_AGENT_PROMPT
import asyncio

flight_llm = setting.GEMINI_MODEL
secret_key = setting.GEMINI_API_KEY

if not secret_key:
    raise ValueError(f"Api key not provided")

flight_model = ChatGoogleGenerativeAI(
    model = flight_llm,
    api_key = secret_key
)

def flight_agent(state: AgentState): 
    input_query = state.get("user_query", "")
    try:
        airports = asyncio.run(aviation_mcp(
            "list_airports"
        ))

        airlines = asyncio.run(aviation_mcp(
            "list_airlines"
        ))
        print("airports", airports)
        print("airlines", airlines)

        prompt = FLIGHT_AGENT_PROMPT.format(
            query=input_query,
            airport_data = str(airports)[:300],
            airline_data = str(airlines)[:300]
        )

        response = flight_model.invoke([
            SystemMessage(content="You are an expert travel flight planner"),
            HumanMessage(content=prompt)
        ])

        flight_data = response.content

    except Exception as e:
        flight_data = f"flight informatioin unavailable {str(e)}"

    return {
        "flight_result": flight_data,
        "messages": [AIMessage(content="flight recommendations generated")]
    }