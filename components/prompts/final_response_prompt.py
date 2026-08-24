from langchain_core.prompts import PromptTemplate


response_prompt = PromptTemplate(
    input_variables = [
        "user_query",
        "travellers",
        "flight_results",
        "hotel_results",
        "weather_results",
        "itinerary"
    ],
template = """
    Generate the final travel response for the user.

    User Request:
    {user_query}

    Number of travellers:
    {travellers}

    Flights:
    {flight_result}

    Hotels:
    {hotel_result}

    Weather:
    {weather_result}

    Itinerary:
    {itinerary_result}

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
)