"""Data processing tool for analyzing and extracting insights."""

from crewai.tools import tool
import re
from collections import Counter

@tool("Data Processing Tool")
def processing_tool(text: str) -> str:
    """
    Process and analyze text data to extract key information and insights.
    
    Args:
        text (str): The text to process
    
    Returns:
        str: Analysis results with key information extracted
    """
    try:
        # Basic statistics
        word_count = len(text.split())
        char_count = len(text)
        
        # Extract potential key phrases (simple approach)
        # Look for phrases in quotes or after markers like "important:", "key:", etc.
        key_phrases = []
        
        # Find quoted text
        quotes = re.findall(r'"([^"]*)"', text)
        key_phrases.extend(quotes[:5])  # Limit to top 5
        
        # Find sentences with key markers
        markers = ['important', 'key', 'critical', 'essential', 'significant', 'main']
        sentences = text.split('.')
        for sentence in sentences:
            if any(marker in sentence.lower() for marker in markers):
                key_phrases.append(sentence.strip())
                if len(key_phrases) >= 10:
                    break
        
        # Extract numbers and statistics
        numbers = re.findall(r'\d+(?:\.\d+)?(?:%|\s*percent|\s*million|\s*billion|\s*thousand)?', text)
        stats = numbers[:10] if numbers else []
        
        # Word frequency (excluding common words)
        common_words = set(['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'is', 'are', 'was', 'were', 'be', 'been', 'being'])
        words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
        word_freq = Counter([w for w in words if w not in common_words])
        top_words = word_freq.most_common(10)
        
        # Format results
        result = f"""
Text Analysis Results:
======================

Basic Statistics:
- Word count: {word_count}
- Character count: {char_count}

Top Keywords:
{chr(10).join([f"- {word}: {count} occurrences" for word, count in top_words[:5]])}

Key Phrases Found:
{chr(10).join([f"- {phrase[:100]}" for phrase in key_phrases[:5]])}

Statistics/Numbers Mentioned:
{chr(10).join([f"- {stat}" for stat in stats[:5]])}
"""
        
        return result
    
    except Exception as e:
        return f"Error processing text: {str(e)}"

def create_processing_tool():
    """Create and return the processing tool."""
    return processing_tool
