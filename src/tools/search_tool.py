"""Search tool for finding information on the web."""

from crewai.tools import tool
from duckduckgo_search import DDGS
import os
import time

@tool("Web Search Tool")
def search_tool(query: str) -> str:
    """
    Search the web for information on a given query.
    
    Args:
        query (str): The search query
    
    Returns:
        str: Search results with titles, URLs, and snippets
    """
    try:
        max_results = int(os.getenv("MAX_SEARCH_RESULTS", 3))
        request_delay = float(os.getenv("REQUEST_DELAY", 2.0))
        
        # Add delay to prevent rate limiting
        time.sleep(request_delay)
        
        # Use DuckDuckGo for web search
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))
        
        if not results:
            return f"No results found for query: {query}"
        
        # Format results
        formatted_results = []
        for i, result in enumerate(results, 1):
            formatted_results.append(
                f"{i}. {result.get('title', 'N/A')}\n"
                f"   URL: {result.get('href', 'N/A')}\n"
                f"   {result.get('body', 'N/A')}\n"
            )
        
        return "\n".join(formatted_results)
    
    except Exception as e:
        return f"Error performing search: {str(e)}"

def create_search_tool():
    """Create and return the search tool."""
    return search_tool
