import uuid
from components.graph.workflow import trip_graph
from components.graph.state import initial_state


def run_trip_planner_agent(user_query: str, thread_id: str | None):
    if not thread_id:
        thread_id = f"user_{uuid.uuid4().hex}"

    config = {"configurable": {
        "thread_id": thread_id
        }
    }


    final_state = trip_graph.invoke(
        initial_state(user_query), #no {} because they create a set and langgraph cannot use them gives error-2
        config = config
    )

    final_result = final_state['messages'][-1].content

    return {
        "thread_id": thread_id,
        "final_result": final_result,
        "flight_result": final_state.get("flight_result", ""),
        "hotel_result": final_state.get("hotel_result", ""),
        "itineary_result": final_state.get("itineary_result", ""),
        "travellers": final_state.get("travellers", "")
    }