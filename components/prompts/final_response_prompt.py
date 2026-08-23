from components.graph.state import AgentState


def response_prompt(state: AgentState):
    return  f"""
    Generate the final travel response for the user.

    User Request:
    {AgentState['user_query']}

    Flights:
    {AgentState['flight_results']}

    Hotels:
    {AgentState['hotel_results']}

    Weather:
    {AgentState['weather_results']}

    Itinerary:
    {AgentState['itinerary']}

    Format the final answer beautifully using these sections:

    1. Trip Summary
    2. Flight Information
    3. Hotel Suggestions
    4. Weather Information
    5. Day-by-Day Itinerary
    6. Estimated Budget
    7. Final Recommendations

    Important:
    - Be clear and practical.
    - Mention that live flight API may not provide ticket prices if pricing is unavailable.
    - Include weather-based travel advice.
    - Keep the response useful for real travel planning.
"""