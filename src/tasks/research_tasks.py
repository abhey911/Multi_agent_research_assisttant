"""Research task definitions for the multi-agent system."""

from crewai import Task

def create_research_tasks(agents, task_config, topic):
    """
    Create all research tasks for the crew.
    
    Args:
        agents (dict): Dictionary of agent instances
        task_config (dict): Task configuration from YAML
        topic (str): Research topic
    
    Returns:
        list: List of Task instances
    """
    
    # Research Task
    research_task = Task(
        description=task_config.get('research', {}).get('description', '').format(topic=topic),
        agent=agents['researcher'],
        expected_output=task_config.get('research', {}).get('expected_output', ''),
    )
    
    # Analysis Task
    analysis_task = Task(
        description=task_config.get('analyze', {}).get('description', '').format(topic=topic),
        agent=agents['analyzer'],
        expected_output=task_config.get('analyze', {}).get('expected_output', ''),
        context=[research_task]  # Depends on research task
    )
    
    # Writing Task
    writing_task = Task(
        description=task_config.get('write', {}).get('description', '').format(topic=topic),
        agent=agents['writer'],
        expected_output=task_config.get('write', {}).get('expected_output', ''),
        context=[research_task, analysis_task]  # Depends on both previous tasks
    )
    
    # Review Task
    review_task = Task(
        description=task_config.get('review', {}).get('description', '').format(topic=topic),
        agent=agents['critic'],
        expected_output=task_config.get('review', {}).get('expected_output', ''),
        context=[writing_task]  # Depends on writing task
    )
    
    return [research_task, analysis_task, writing_task, review_task]
