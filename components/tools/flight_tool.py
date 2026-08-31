from components.prompts.flight_prompt import FLIGHT_AGENT_PROMPT
from components.graph.state import AgentState
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from config import setting
import asyncio
from components.mcp_client.mcp_clients import client


flight_llm = setting.GEMINI_MODEL
secret_key = setting.GEMINI_API_KEY

if not secret_key:
    raise ValueError(f"Api key not provided")

flight_model = ChatGoogleGenerativeAI(
    model = flight_llm,
    api_key = secret_key
)

flight_tool = {}

async def initialize_tool():
    "This function will list all the available tools"
    global flight_tool

    if flight_tool:
        return

    tools = await client.get_tools()

    print(f"Avaiable tools")

    for tool in tools:
        print(tool.name)
    
    flight_tool = {
        tool.name: tool
        for tool in tools
        if tool.name != "tavily_search_tool"
    }

async def aviation_mcp(
        tool_name: str,
        tool_args: dict = None
):
    "This function will search airlines and airports"
    tools = await client.get_tools()

    tool = next(
        t for t in tools
        if t.name == tool_name
    )

    result = await tool.ainvoke(
        tool_args or {}
    )

    return result

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
            airport_data = str(airports)[:100],
            airline_data = str(airlines)[:100]
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