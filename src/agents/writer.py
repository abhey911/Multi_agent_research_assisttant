"""Writer Agent - Creates comprehensive research reports."""

from crewai import Agent
from src.utils import load_config
from src.utils.llm_factory import create_llm

conf = load_config()


def create_writer_agent(config, llm=None):
    """
    Create and configure the Writer Agent.
    
    Args:
        config (dict): Agent configuration from YAML
        llm: Language model instance (optional)
    
    Returns:
        Agent: Configured writer agent
    """
    if llm is None:
        llm = create_llm(conf, temperature=0.5)
    
    # Get agent configuration
    agent_config = config.get('writer', {})
    
    # Create agent (no tools needed, focuses on writing)
    agent = Agent(
        role=agent_config.get('role', 'Technical Writer'),
        goal=agent_config.get('goal', 'Create clear, comprehensive research reports on {topic}'),
        backstory=agent_config.get('backstory', 'You are an experienced technical writer.'),
        tools=[],
        llm=llm,
        verbose=agent_config.get('verbose', True),
        allow_delegation=agent_config.get('allow_delegation', False),
        max_iter=agent_config.get('max_iterations', 2),
        memory=True
    )
    
    return agent
