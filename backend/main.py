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

    final_state = None 

    for state in trip_graph.stream(
        initial_state(user_query), #no {} because they create a set and langgraph cannot use them gives error-2
        config = config,
        stream_mode="values"
    ):
        print("\n" + "=" * 80)
        print("State after node execution")
        print("=" * 80)

        for key, value in state.items():
            if key == 'messages':
                print(f"{key}: ")
                for message in value:
                    print(f" [{message.type}] {message.content}")
            else:
                print(f"{key}: {value}")

        final_state = state

    final_result = final_state['messages'][-1].content

    return {
        "thread_id": thread_id,
        "answer": final_result,
        "flight_results": final_state.get("flight_result", ""),
        "hotel_results": final_state.get("hotel_result", ""),
        "itinerary": final_state.get("itinerary_result", ""),
    }