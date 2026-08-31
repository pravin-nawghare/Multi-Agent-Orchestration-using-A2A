import os
import asyncio
from config import setting
from langchain_mcp_adapters.client import MultiServerMCPClient

#creating web search mcp client
tavily_api_key = setting.TAVILY_API_KEY
aviationstack_api_key = setting.AVIATIONSTACK_API_KEY

client = MultiServerMCPClient( # add all mcp related code here
    { # MCP client for internet search operations
        "tavily" : { #name can be anything, it just tell whose server we have created
            "transport": "streamable_http", # for remote server
            "url": f"https://mcp.tavily.com/mcp/?tavilyApiKey={tavily_api_key}"
        },

        "aviation_stack": { # for flight search operation
            "transport": "stdio", # for local server
            "command": "uvx",
            "args": [
                "--with",
                "mcp<2", # aviationstack-mcp currently depends on MCP v1 API
                "aviationstack-mcp"
            ],
            "env": {
                "AVIATION_STACK_API_KEY": aviationstack_api_key
            }
        }
    }
)