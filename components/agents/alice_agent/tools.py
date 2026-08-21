AVAILABILITY = {
    "2026-08-16":"Available from 4 pm to 6 pm",
    "2026-08-17" : "Available from 10 am to 12 pm",
    "2026-08-18" : "Available all afternoon from 1 pm to 3 pm",
    "2026-08-19" : "Busy all day"
}

def get_availablity(date_str: str) -> dict[str, str]:
    """
    Simulates checking Alice's availability on a specific date.

    Args:
        date_str (str): A date in 'YYYY-MM-DD' format.

    Returns:
        dict: A small JSON-like dictionary with availability info.
    """

    if not date_str:
        return {"status": "error", "message": "No date provided."}

    availability = AVAILABILITY.get(date_str)

    if availability:
        return {
            "status": "completed",
            "message": f"On {date_str}, Alice is {availability}.",
        }

    return {
        "status": "input_required",
        "message": f"She is not available on {date_str}. Please ask about another date.",
    }