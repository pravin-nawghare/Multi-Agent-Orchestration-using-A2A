import sqlite3
from pathlib import Path
from components.graph.state import AgentState
from components.agents.travel_agent.final_response_agent import final_response
from components.agents.travel_agent.itinerary_agent import itineary_agent
from components.agents.travel_agent.flight_agent import flight_agent
from components.agents.travel_agent.hotel_agent import hotel_agent
from langgraph.graph import START, END, StateGraph
from langgraph.checkpoint.sqlite import SqliteSaver

# to sove error 1 which was checkpoint storage folder was not getting created
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# D:\Data-Sorting\Projects\Multi-Agent-Orchestration-using-A2A\db
DB_DIR = PROJECT_ROOT / "db"

# Create directory if it doesn't exist
DB_DIR.mkdir(parents=True, exist_ok=True)

# Full database path
DB_PATH = DB_DIR / "langgraph_checkpoints.sqlite"

print(f"LangGraph checkpoint DB: {DB_PATH}")
# till this point the code was added
connection = sqlite3.connect(
    str(DB_PATH),
    check_same_thread = False
)
custom_checkpointer = SqliteSaver(connection)

graph = StateGraph(AgentState)
# add nodes -> agents that defined
graph.add_node("flight_node", flight_agent)
graph.add_node("hotel_node", hotel_agent)
graph.add_node("itinerary_node", itineary_agent)
graph.add_node("response_node", final_response)

# add edges -> connection between nodes
graph.add_edge(START, "flight_node")
graph.add_edge("flight_node", "hotel_node")
graph.add_edge("hotel_node", "itinerary_node")
graph.add_edge("itinerary_node", "response_node")
graph.add_edge("response_node", END)

trip_graph = graph.compile(checkpointer=custom_checkpointer)