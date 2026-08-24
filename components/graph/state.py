# Shared state definition for Travel Agent.

from datetime import datetime, date, timedelta
from dateutil import parser
from typing import Annotated, TypedDict
from langchain_core.messages import AnyMessage, HumanMessage
import operator



# The main agent state class
class AgentState(TypedDict):

    messages: Annotated[list[AnyMessage], operator.add]
    user_query: str
    flight_result: str
    weather_result: str
    hotel_result: str
    itineary_result: str
    approved: bool
    travellers: int | None = 2
    start_date: str | None   # ISO 8601 format -> "2026-08-31"
    

def initial_state(query: str, tourist_count: int = 2) -> dict:
    """
    Creates an initial state for Langgraph workflow.

    Args:
        query: User input message
        tourist_count: Number of people travelling
        
    Returns:
        Returns a plain dict as initial state
    """
    try: # convert given into iso format
        dt = parser.parse(query, fuzzy=True)
        formatted_date = dt.date().isoformat()
    except(ValueError, OverflowError): # no date provided then 2 day's after date is used by default
        default_date = date.today() + timedelta(days=2)
        formatted_date = default_date.isoformat()

    return {
        "messages": [],
        "user_query": query,
        "flight_result": "",
        "weather_result": "",
        "hotel_result": "",
        "itineary_result": "",
        "approved": False,
        "travellers": tourist_count,
        "start_date": str
    }