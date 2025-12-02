"""Helper utilities for the multi-agent research system."""

import re
import os
from datetime import datetime
from pathlib import Path

def save_report(content, topic, output_dir=None):
    """
    Save research report to file.
    
    Args:
        content (str): Report content in markdown format
        topic (str): Research topic (used for filename)
        output_dir (str): Directory to save report (default: outputs/reports)
    
    Returns:
        str: Path to saved file
    """
    if output_dir is None:
        # Get the project root directory
        current_dir = Path(__file__).parent.parent.parent
        output_dir = current_dir / "outputs" / "reports"
    else:
        output_dir = Path(output_dir)
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Create filename from topic
    filename = clean_filename(topic)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = output_dir / f"{filename}_{timestamp}.md"
    
    # Save report
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return str(filepath)

def clean_filename(text):
    """
    Clean text to create valid filename.
    
    Args:
        text (str): Text to clean
    
    Returns:
        str: Cleaned filename
    """
    # Remove invalid characters
    text = re.sub(r'[<>:"/\\|?*]', '', text)
    # Replace spaces with underscores
    text = text.replace(' ', '_')
    # Limit length
    text = text[:100]
    # Remove leading/trailing underscores
    text = text.strip('_')
    return text.lower()

def format_timestamp(dt=None):
    """
    Format datetime object as readable timestamp.
    
    Args:
        dt (datetime): Datetime object (default: current time)
    
    Returns:
        str: Formatted timestamp
    """
    if dt is None:
        dt = datetime.now()
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def clean_text(text):
    """
    Clean text by removing extra whitespace and special characters.
    
    Args:
        text (str): Text to clean
    
    Returns:
        str: Cleaned text
    """
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Remove leading/trailing whitespace
    text = text.strip()
    return text

def extract_section(text, section_title):
    """
    Extract a specific section from markdown text.
    
    Args:
        text (str): Full markdown text
        section_title (str): Title of section to extract
    
    Returns:
        str: Extracted section content or empty string if not found
    """
    # Match section with various header levels
    pattern = rf'#+\s*{re.escape(section_title)}.*?\n(.*?)(?=\n#+\s|\Z)'
    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    
    if match:
        return match.group(1).strip()
    return ""

def count_words(text):
    """
    Count words in text.
    
    Args:
        text (str): Text to count
    
    Returns:
        int: Word count
    """
    # Remove markdown syntax for more accurate count
    text = re.sub(r'[#*`\[\]()]', '', text)
    words = text.split()
    return len(words)

def truncate_text(text, max_length=500, suffix="..."):
    """
    Truncate text to maximum length.
    
    Args:
        text (str): Text to truncate
        max_length (int): Maximum length
        suffix (str): Suffix to add if truncated
    
    Returns:
        str: Truncated text
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix
