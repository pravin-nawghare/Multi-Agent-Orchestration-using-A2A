from config import setting

from components.mcp_client.mcp_clients import client


async def _get_tavily_search_tool(tavily_client):
    "This function load tavily search tool"
    "Args: client"
    tools = await tavily_client.get_tools()
    tool_map = {tool.name: tool for tool in tools}
    try:
        return tool_map.get("tavily_search")
    except Exception as e:
        print(f"Error occured while web search tool initialization: {str(e)}")


async def web_search(query: str):
    tool = await _get_tavily_search_tool(tavily_client=client)
    try:
        result = await tool.ainvoke(
            {
                "query": query
            }
        )
        return result
    except Exception as e:
        print(f"Error while doing internet search: {str(e)}")