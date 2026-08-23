from components.graph.state import AgentState


def itineary_agent_prompt(state: AgentState):
    return f"""
    Create a complete travel itinerary.

    User Query:
    {state['user_query']}

    Flight Results:
    {state['flight_result']}

    Hotel Results:
    {state['hotel_result']}

    Weather Results:
    {state['weather_result']}

    Make the itinerary practical, budget-aware, and easy to follow.
    """

