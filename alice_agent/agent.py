# Langchain/Langgraph
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langgraph.checkpoint.memory import MemorySaver 
from langchain_core.messages import HumanMessage, AIMessage
from tools import get_availablity
import asyncio

load_dotenv()


class AliceAgent():
    def __init__(self):
        self.model = "gemini-2.5-flash"
        self.tools = [get_availablity] if get_availablity else []
        self.system_message = """
            You are Alice's scheduling assistant. Your only job is to use the "get_availability" too to answer 
            questions about Alice's schedule for trip planning.
            If the question is unrelated to scheduling politely say you can't help.
        """
        self.checkpoint = MemorySaver()
        
        self.agent = create_agent(
            model=ChatGoogleGenerativeAI(model=self.model,temperature=0.2),
            tools=self.tools,
            system_prompt=self.system_message,
            checkpointer=self.checkpoint
        )
    async def get_response(self, query: str, context_id):
        config = {"configurable": {
                        "thread_id": context_id
                    }
                }

        inputs = {
            "messages": HumanMessage(content=query)
        }

        raw_result = self.agent.invoke(inputs, config)
        messages = raw_result.get("messages", [])
        ai_message = [message.content for message in messages if isinstance(message, AIMessage)]
        response = ai_message[-1] if ai_message else "No Response"
        return response

agent = AliceAgent()
response = asyncio.run(agent.get_response(query="When does Alice is available on 17 August 2026", context_id="test-1"))
print(response)