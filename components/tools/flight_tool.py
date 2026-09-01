from langchain_google_genai import ChatGoogleGenerativeAI
from config import setting
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

