"""Analyzer Agent - Processes and evaluates research data."""

from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from ..tools import create_processing_tool

from src.utils import load_config

conf = load_config()


def create_analyzer_agent(config, llm=None):
    """
    Create and configure the Analyzer Agent.
    
    Args:
        config (dict): Agent configuration from YAML
        llm: Language model instance (optional)
    
    Returns:
        Agent: Configured analyzer agent
    """
    if llm is None:
        llm = ChatGoogleGenerativeAI(
            model=conf.gemini_model_flash,
            temperature=0.5,
            convert_system_message_to_human=True
        )
    
    # Get agent configuration
    agent_config = config.get('analyzer', {})
    
    # Create tools
    processing_tool = create_processing_tool()
    
    # Create agent
    agent = Agent(
        role=agent_config.get('role', 'Data Analyst'),
        goal=agent_config.get('goal', 'Extract insights from research findings on {topic}'),
        backstory=agent_config.get('backstory', 'You are a skilled analyst.'),
        tools=[processing_tool],
        llm=llm,
        verbose=agent_config.get('verbose', True),
        allow_delegation=agent_config.get('allow_delegation', False),
        max_iter=agent_config.get('max_iterations', 5),
        memory=True
    )
    
    return agent
