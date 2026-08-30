from config import setting

from tavily import TavilyClient

client = TavilyClient(
    api_key = setting.TAVILY_API_KEY
)

def internet_search(query: str, result: int = 5):
    try:
        response = client.search(
            query = query,
            max_results = result
        )
        # print(f"Inside web search tool")
        results = []

        # extract title, url and text response from web search result
        for i, r in enumerate(response["results"], 1):
            title   = r.get("title", "Unknown") 
            url     = r.get("url", "")
            snippet = r.get("content", "").strip()
        # Keep only the first 300 characters to prevent context overflow
            if len(snippet) > 300:
                snippet = snippet[:300].rsplit(" ", 1)[0] + "..."

            results.append(f"{i}. **{title}**\n   {url}\n   {snippet}")

        return "\n\n".join(results) 

    except Exception as e:
        print(f"Error occured during web search: {str(e)}")