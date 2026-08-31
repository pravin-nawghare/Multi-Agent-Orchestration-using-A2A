import os
import asyncio
from config import setting
from langchain_mcp_adapters.client import MultiServerMCPClient

#creating web search mcp client
tavily_api_key = setting.TAVILY_API_KEY

client = MultiServerMCPClient( # add all mcp related code here
    { # MCP client for internet search operations
        "tavily" : { #name can be anything, it just tell whose server we have created
            "transport": "streamable_http", # for remote server
            "url": f"https://mcp.tavily.com/mcp/?tavilyApiKey={tavily_api_key}"
        },
    }
)