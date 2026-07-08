from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVLIY_API_KEY"))

def search_tavily(query):
    """You are a helpful assistant that searches the web using Tavily 
            and returns the top 5 results with titles, URLs, and snippets."""
    try:
        response = client.search(
            query=query,
            max_results=5
            )
        results = []
        for i, r in enumerate(response["results"], 1):
            title = r.get("title", "No title")
            url = r.get("url", "No URL")
            snippet = r.get("content", "No snippet")

            if len(snippet) > 300:
                snippet = snippet[:300] + "..."
            results.append(f"{i}. {title}\nURL: {url}\nSnippet: {snippet}\n")
        return "\n\n".join(results)
    except Exception as e:
        print(f"Error searching Tavily: {e}")
        return None
