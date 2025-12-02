"""Web scraping tool for extracting content from URLs."""

from crewai.tools import tool
import requests
from bs4 import BeautifulSoup
import re

@tool("Web Scraping Tool")
def scraping_tool(url: str) -> str:
    """
    Scrape and extract main content from a web page.
    
    Args:
        url (str): The URL to scrape
    
    Returns:
        str: Extracted text content from the page
    """
    try:
        # Set headers to mimic a browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Fetch the page
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style", "nav", "footer", "header"]):
            script.decompose()
        
        # Get text content
        text = soup.get_text()
        
        # Clean up text
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        # Limit text length
        if len(text) > 5000:
            text = text[:5000] + "..."
        
        return f"Content from {url}:\n\n{text}"
    
    except requests.exceptions.RequestException as e:
        return f"Error scraping {url}: {str(e)}"
    except Exception as e:
        return f"Error processing {url}: {str(e)}"

def create_scraping_tool():
    """Create and return the scraping tool."""
    return scraping_tool
