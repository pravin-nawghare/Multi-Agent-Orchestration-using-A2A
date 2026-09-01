# from langchain_core.messages.ai import AIMessage
# result = {
    # 'model': 
    # {'messages': 
    #     [AIMessage(
    #         content=
    #             "Hello! I'm doing well, thank you.\n\nHow can I help you today with your scheduling needs?", 
    #             additional_kwargs={}, 
    #             response_metadata=
    #                 {
    #                     'finish_reason': 'STOP', 
                    #     'model_name': 'gemini-2.5-flash', 
                    #     'safety_ratings': [], 
                    #     'model_provider': 'google_genai'
                    # }, 
                    #     id='lc_run--019ffacb-2705-7470-a8bc-9461e28e5fad-0', 
                    #     tool_calls=[], 
                    #     invalid_tool_calls=[], 
                    #     usage_metadata={
                    #         'input_tokens': 16, 
                            # 'output_tokens': 51, 
                            # 'total_tokens': 67, 
                            # 'input_token_details': 
                            #     {
                            #         'cache_read': 0
                            #     }, 
                            #     'output_token_details': 
                            #         {
                            #             'reasoning': 28
                #                     }
                #                 }
                #             )
                #         ]
                #     }
                # }
# print(result['model']['messages'][0].content)

#  LLM response with tools

# {'messages': [HumanMessage(content='When does Alice is available on 17 August 2026', additional_kwargs={}, 
# response_metadata={}, id='4f39553b-b1ae-4e4a-b49d-258b3867fca0'), AIMessage(content='', 
# additional_kwargs={'function_call': {'name': 'get_availablity', 'arguments': '{"date_str": "2026-08-17"}'},
# '__gemini_function_call_thought_signatures__': {'bfd22efe-785b-4a96-be37-a7a7c7604143': 
# 'Cs8CARFNMg8wpaxFwXkz9U3/QbSouxJE1ep2WgI6zZ9vUipEMtROvSa0g8guCyQ2ZKblmBvs46kQ1vVO/fdjWHxiyTKKz2WmEshE6vxXj5Xom
# 8aE+0c9123VzK0ARptMCCnMzzUhdPh4ltxmAViVkVD0243qS9fE81gaP1J68sAZ7amLbjsfdXGzJjwBBqvY8oL7JxC6Yat1C6/J2suJGf8x5Jj
# MZU/8CppwVrhbbHYiZr0kb064LWlQhTeOu6YVPudiOHEwxckc1rRpzjAFiCfEj16iocjIhlCppuGS3A0nmt79Yv9kLSmY2ROLbjZbB3rHG5wtu
# zcCf9qP46pRtPriKSViT/z+1kJIG0vzYP3knN0lm2wbZm5PbzD6519kH66kS3dL4rxO3KWa3h9KGi4wx5iDW9zsS+8SvW8hkZlhss1mqv+zQMk
# AKf0FsTiq0hU='}}, response_metadata={'finish_reason': 'STOP', 'model_name': 'gemini-2.5-flash', 
# 'safety_ratings': [], 'model_provider': 'google_genai'}, id='lc_run--019ffb36-76bf-7b11-af9a-f50de02fddd9-0', 
# tool_calls=[{'name': 'get_availablity', 'args': {'date_str': '2026-08-17'}, 'id': 
# 'bfd22efe-785b-4a96-be37-a7a7c7604143', 'type': 'tool_call'}], invalid_tool_calls=[], 
# usage_metadata={'input_tokens': 165, 'output_tokens': 121, 'total_tokens': 286, 'input_token_details': 
# {'cache_read': 0}, 'output_token_details': {'reasoning': 93}}), ToolMessage(content='{"status": "completed",
#  "message": "On 2026-08-17, Alice is Available from 10 am to 12 pm."}', name='get_availablity', 
#  id='1062e04c-a4f2-4277-89f8-07d44b34af74', tool_call_id='bfd22efe-785b-4a96-be37-a7a7c7604143'), 
#  AIMessage(content=[{'type': 'text', 'text': 'On 2026-08-17, Alice is Available from 10 am to 12 pm.', 
#  'extras': {'signature': 'Cq0CARFNMg801QeTuV2lwvCEuxDUcx1IriFcSvqEyTcuUs0XGqBlzseQbcN9ycuej8kjmMtxffTMhpTzVW3u
#  05nV5yqfh+cxpjDoGwwawVEfQ0RVndxyV8+LXdSbpvko0LdnKTxqiH8VgAScAKZxYiOcA0ZNMwQKYpof+UpDS3CH5RQnRc5CYQnkiJKFZhNip
#  sF2AiD6TXPjUysKHq+Hq362Gw+cm1AU0WPWmaM8K1dAEIc4GsQTz5LAMU7C0guTXpyBxwZoA7/SxTWuEfHc7TxdRou+tWBjGK1lreC3nmjIQD
#  E9mZW8E3NFOfP4C3hq7lmw1JJNRYpFCoGrCiGyyn3KIfkXKq6iym2y5ttf3qwZTKURkxYEEPm5Vk/8qqn0aX3c0lLJxJOYFRMe5lucdg=='}}], 
#  additional_kwargs={}, response_metadata={'finish_reason': 'STOP', 'model_name': 'gemini-2.5-flash', 
#  'safety_ratings': [], 'model_provider': 'google_genai'}, id='lc_run--019ffb36-7ee1-72c3-8cb8-1b5d46713148-0', 
#  tool_calls=[], invalid_tool_calls=[], usage_metadata={'input_tokens': 241, 'output_tokens': 123, 
#  'total_tokens': 364, 'input_token_details': {'cache_read': 0}, 'output_token_details': {'reasoning': 96}})]}
# from backend.main import run_trip_planner_agent
# from config import setting

# id = "test-2"
# user_input = input("Enter travel request: ")
# response = run_trip_planner_agent(user_input,thread_id=None)

#print("Final Respopnse\n")
#print(response['answer'])

# from components.tools.websearch_tool import web_search, _get_tavily_search_tool
# from components.prompts.flight_prompt import FLIGHT_AGENT_PROMPT
# from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
# from langchain_google_genai import ChatGoogleGenerativeAI
from config import setting
import asyncio
from components.mcp_client.mcp_clients import client
# import nest_asyncio
# nest_asyncio.apply()

# async def get_all_tools():
#     tools = await client.get_tools()
#     print(f"Available tools:")
#     for tool in tools:
#         print(tool.name)

# asyncio.run(get_all_tools()) 

# web_response = asyncio.run(web_search(query="What is the latest development happended in Amazon Rain forest"))
# print(web_response)

# result = asyncio.run(_get_tavily_search_tool(client))
# print(type(result))
# print(result)

# async def get_all_tools():
#     tools = await client.get_tools()
#     return tools

# mcp_tools = asyncio.run(get_all_tools()) 
# for tool in mcp_tools:
#     print(tool.name)

# search_tool = None
# flight_tool = {}

# async def initialize_tool():
#     global search_tool
#     global flight_tool

#     if search_tool is not None and flight_tool:
#         return

#     tools = await client.get_tools()

#     print(f"Avaiable tools")

#     for tool in tools:
#         print(tool.name)

#     search_tool = next(
#         tool
#         for tool in tools
#         if tool.name == "tavily_search_tool"
#     )

#     flight_tool = {
#         tool.name: tool
#         for tool in tools
#         if tool.name != "tavily_search_tool"
#     }
# async def aviation_mcp(
#         tool_name: str,
#         tool_args: dict = None
# ):
#     tools = await client.get_tools()

#     tool = next(
#         t for t in tools
#         if t.name == tool_name
#     )

#     result = await tool.ainvoke(
#         tool_args or {}
#     )

#     return result
# llm = ChatGoogleGenerativeAI(model = setting.GEMINI_MODEL)
# def flight_agent(query: str): # state: AgentState
    # print("Inside flight agent")

    # input_query = query#state.get("user_query", "")
    # try:
    #     airports = asyncio.run(aviation_mcp(
    #         "list_airports"
    #     ))

    #     airlines = asyncio.run(aviation_mcp(
    #         "list_airlines"
    #     ))
    #     print("airports", airports)
    #     print("airlines", airlines)

    #     prompt = FLIGHT_AGENT_PROMPT.format(
    #         query=input_query,
    #         airport_data = str(airports)[:100],
    #         airline_data = str(airlines)[:100]
    #     )

    #     response = llm.invoke([
    #         SystemMessage(content="You are an expert travel flight planner"),
    #         HumanMessage(content=prompt)
    #     ])

    #     flight_data = response.content

    # except Exception as e:
    #     flight_data = f"flight informatioin unavailable {str(e)}"

    # return {
        # "flight_result": flight_data,
    #     "messages": AIMessage(content="flight recommendations generated")
    # }
# flight_info = flight_agent(query="Search flights from New Delhi to New York City")
# print(flight_info)

import asyncio
import os
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from config import setting


async def main():

    server_params = StdioServerParameters(
    command=r"C:\Users\prave\anaconda3\envs\travel\python.exe",
    args=[
        "-m",
        "components.custom_mcp_server.weather_mcp_server",
    ],
    cwd=r"D:\Data-Sorting\Projects\Multi-Agent-Orchestration-using-A2A",
)


if __name__ == "__main__":
    asyncio.run(main())


