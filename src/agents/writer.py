"""Writer Agent - Creates comprehensive research reports."""

from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI

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
        llm = ChatGoogleGenerativeAI(
            model="gemini/gemini-1.5-pro",
            temperature=0.7,
            convert_system_message_to_human=True
        )
    
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
        max_iter=agent_config.get('max_iterations', 3),
        memory=True
    )
    
    return agent
