"""Critic Agent - Reviews and provides quality assurance."""

from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI

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
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-pro",
            temperature=0.3,
            convert_system_message_to_human=True
        )
    
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
        max_iter=agent_config.get('max_iterations', 2),
        memory=True
    )
    
    return agent
