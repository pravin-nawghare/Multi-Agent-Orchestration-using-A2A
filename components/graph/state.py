# Shared state definition for Travel Agent.

from typing import Annotated, Any, TypedDict
from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages

# The main agent state class
class AgentState(TypedDict):

    messages: Annotated[list[AnyMessage], add_messages]
    user_query: str
    flight_result: str
    weather_result: str
    hotel_result: str
    itineary_result: str
    approved: bool
    travellers: int
    

def initial_state(query: str, tourist_count: int) -> dict:
    """
    Creates an initial state for Langgraph workflow.

    Args:
        query: User input message
        tourist_count: Number of people travelling
        
    Returns:
        Returns a plain dict as initial state
    """
    return {
        "messages": [],
        "user_query": query,
        "flight_result": "",
        "weather_result": "",
        "hotel_result": "",
        "itineary_result": "",
        "approved": False,
        "travellers": tourist_count
    }