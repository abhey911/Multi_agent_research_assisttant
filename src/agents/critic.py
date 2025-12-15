"""Critic Agent - Reviews and provides quality assurance."""

from crewai import Agent
from src.utils import load_config
from src.utils.llm_factory import create_llm

conf = load_config()


def create_critic_agent(config, llm=None):
    """
    Create and configure the Critic Agent.
    
    Args:
        config (dict): Agent configuration from YAML
        llm: Language model instance (optional)
    
    Returns:
        Agent: Configured critic agent
    """
    if llm is None:
        llm = create_llm(conf, temperature=0.2)
    
    # Get agent configuration
    agent_config = config.get('critic', {})
    
    # Create agent (no tools needed, focuses on review)
    agent = Agent(
        role=agent_config.get('role', 'Quality Assurance Specialist'),
        goal=agent_config.get('goal', 'Ensure research reports on {topic} are accurate and high-quality'),
        backstory=agent_config.get('backstory', 'You are a meticulous reviewer.'),
        tools=[],
        llm=llm,
        verbose=agent_config.get('verbose', True),
        allow_delegation=agent_config.get('allow_delegation', False),
        max_iter=agent_config.get('max_iterations', 1),
        memory=True
    )
    
    return agent
