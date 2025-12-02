"""Researcher Agent - Gathers information from various sources."""

from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from ..tools import create_search_tool, create_scraping_tool

def create_researcher_agent(config, llm=None):
    """
    Create and configure the Researcher Agent.
    
    Args:
        config (dict): Agent configuration from YAML
        llm: Language model instance (optional)
    
    Returns:
        Agent: Configured researcher agent
    """
    if llm is None:
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            temperature=0.7
        )
    
    # Get agent configuration
    agent_config = config.get('researcher', {})
    
    # Create tools
    search_tool = create_search_tool()
    scraping_tool = create_scraping_tool()
    
    # Create agent
    agent = Agent(
        role=agent_config.get('role', 'Research Specialist'),
        goal=agent_config.get('goal', 'Gather comprehensive information on {topic}'),
        backstory=agent_config.get('backstory', 'You are an expert researcher.'),
        tools=[search_tool, scraping_tool],
        llm=llm,
        verbose=agent_config.get('verbose', True),
        allow_delegation=agent_config.get('allow_delegation', False),
        max_iter=agent_config.get('max_iterations', 10)
    )
    
    return agent
