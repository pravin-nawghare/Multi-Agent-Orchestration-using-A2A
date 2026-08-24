from langchain_core.prompts import PromptTemplate


itineary_agent_prompt = PromptTemplate(
    input_variables = [
        "user_query",
        "travellers",
        "flight_result",
        "hotel_result",
        "weather_result"
    ],
    template = """
    Create a complete travel itinerary.

    User Query:
    {user_query}

    Number of travellers:
    {travellers}

    Flight Results:
    {flight_result}

    Hotel Results:
    {hotel_result}

    Weather Results:
    {weather_result}

    Make the itinerary practical, budget-aware, and easy to follow.
    """
)

