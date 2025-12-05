"""
Multi-Agent Research Assistant
A Streamlit web interface for the multi-agent research system.
"""

import streamlit as st
import os
from datetime import datetime
from crewai import Crew, Process
from pathlib import Path
from langchain_google_genai import ChatGoogleGenerativeAI

# Add src to path
import sys
sys.path.insert(0, str(Path(__file__).parent / "src"))

from src.agents import (
    create_researcher_agent,
    create_analyzer_agent,
    create_writer_agent,
    create_critic_agent
)
from src.tasks import create_research_tasks
from src.utils import load_config, get_agent_config, get_task_config, save_report

# Page configuration
st.set_page_config(
    page_title="Multi-Agent Research Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .status-box {
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .status-completed {
        background-color: #d4edda;
        border-left: 4px solid #28a745;
    }
    .status-in-progress {
        background-color: #fff3cd;
        border-left: 4px solid #ffc107;
    }
    .status-waiting {
        background-color: #f8f9fa;
        border-left: 4px solid #6c757d;
    }
    .report-section {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

def initialize_session_state():
    """Initialize session state variables."""
    if 'research_completed' not in st.session_state:
        st.session_state.research_completed = False
    if 'report' not in st.session_state:
        st.session_state.report = None
    if 'topic' not in st.session_state:
        st.session_state.topic = ""

def check_configuration():
    """Check if required configuration is present."""
    try:
        config = load_config()
        return True, "Configuration loaded successfully"
    except ValueError as e:
        return False, str(e)

def run_research(topic, research_depth):
    """
    Execute the multi-agent research workflow.
    
    Args:
        topic (str): Research topic
        research_depth (str): Depth of research (quick, standard, deep)
    
    Returns:
        str: Final research report
    """
    try:
        # Load configuration
        config = load_config()
        agent_config = get_agent_config()
        task_config = get_task_config()
        
        # Create status placeholder
        status_placeholder = st.empty()
        
        # Create LLM instances
        status_placeholder.info("🔧 Initializing AI models...")
        
        llm_flash = ChatGoogleGenerativeAI(
            model="gemini/gemini-1.5-flash",
            temperature=0.7,
            convert_system_message_to_human=True
        )
        
        llm_pro = ChatGoogleGenerativeAI(
            model="gemini/gemini-1.5-pro",
            temperature=0.7,
            convert_system_message_to_human=True
        )
        
        # Create agents with LLM instances
        status_placeholder.info("🔧 Creating specialized agents...")
        
        researcher = create_researcher_agent(agent_config, llm_flash)
        analyzer = create_analyzer_agent(agent_config, llm_flash)
        writer = create_writer_agent(agent_config, llm_pro)
        critic = create_critic_agent(agent_config, llm_pro)
        
        agents = {
            'researcher': researcher,
            'analyzer': analyzer,
            'writer': writer,
            'critic': critic
        }
        
        # Create tasks
        status_placeholder.info("📋 Creating research tasks...")
        tasks = create_research_tasks(agents, task_config, topic)
        
        # Create crew
        status_placeholder.info("🚀 Assembling research crew...")
        crew = Crew(
            agents=list(agents.values()),
            tasks=tasks,
            process=Process.sequential,
            verbose=True
        )
        
        # Execute research
        status_placeholder.info("🔍 Research in progress... This may take a few minutes.")
        
        # Run the crew
        result = crew.kickoff()
        
        status_placeholder.success("✅ Research completed successfully!")
        
        return result
        
    except Exception as e:
        st.error(f"Error during research: {str(e)}")
        import traceback
        st.error(traceback.format_exc())
        return None

def main():
    """Main application function."""
    
    # Initialize session state
    initialize_session_state()
    
    # Header
    st.markdown('<div class="main-header">🤖 Multi-Agent Research Assistant</div>', unsafe_allow_html=True)
    st.markdown("---")
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # Check configuration
        config_ok, config_msg = check_configuration()
        if config_ok:
            st.success("✅ " + config_msg)
        else:
            st.error("❌ " + config_msg)
            st.info("Please set up your .env file with required API keys.")
            st.stop()
        
        st.markdown("---")
        
        st.header("📚 About")
        st.markdown("""
        This system uses multiple specialized AI agents:
        - **🔍 Researcher**: Gathers information
        - **📊 Analyzer**: Extracts insights
        - **✍️ Writer**: Creates reports
        - **🔎 Critic**: Ensures quality
        """)
        
        st.markdown("---")
        st.markdown("**Powered by:**")
        st.markdown("- CrewAI")
        st.markdown("- Google Gemini")
        st.markdown("- Streamlit")
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("🎯 Research Query")
        
        # Input form
        with st.form("research_form"):
            topic = st.text_area(
                "Enter your research topic:",
                placeholder="E.g., 'Current state of quantum computing and its applications in cryptography'",
                height=100,
                help="Be specific about what you want to research"
            )
            
            research_depth = st.select_slider(
                "Research Depth:",
                options=["Quick", "Standard", "Deep"],
                value="Standard",
                help="Quick: 5-10 sources, Standard: 10-15 sources, Deep: 15+ sources"
            )
            
            submit_button = st.form_submit_button("🚀 Start Research", use_container_width=True)
        
        if submit_button and topic:
            st.session_state.topic = topic
            st.session_state.research_completed = False
            
            # Run research
            with st.spinner("Research in progress..."):
                result = run_research(topic, research_depth.lower())
                
                if result:
                    st.session_state.report = str(result)
                    st.session_state.research_completed = True
    
    with col2:
        st.header("📊 Progress")
        
        if st.session_state.research_completed:
            st.markdown('<div class="status-box status-completed">✅ Researcher: Completed</div>', unsafe_allow_html=True)
            st.markdown('<div class="status-box status-completed">✅ Analyzer: Completed</div>', unsafe_allow_html=True)
            st.markdown('<div class="status-box status-completed">✅ Writer: Completed</div>', unsafe_allow_html=True)
            st.markdown('<div class="status-box status-completed">✅ Critic: Completed</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="status-box status-waiting">⏳ Researcher: Waiting</div>', unsafe_allow_html=True)
            st.markdown('<div class="status-box status-waiting">⏳ Analyzer: Waiting</div>', unsafe_allow_html=True)
            st.markdown('<div class="status-box status-waiting">⏳ Writer: Waiting</div>', unsafe_allow_html=True)
            st.markdown('<div class="status-box status-waiting">⏳ Critic: Waiting</div>', unsafe_allow_html=True)
    
    # Display results
    if st.session_state.research_completed and st.session_state.report:
        st.markdown("---")
        st.header("📄 Research Report")
        
        # Action buttons
        col1, col2, col3 = st.columns([1, 1, 4])
        
        with col1:
            if st.button("📥 Download Report", use_container_width=True):
                # Save report
                filepath = save_report(st.session_state.report, st.session_state.topic)
                st.success(f"Report saved to: {filepath}")
        
        with col2:
            if st.button("📋 Copy to Clipboard", use_container_width=True):
                st.code(st.session_state.report, language="markdown")
        
        # Display report
        with st.container():
            st.markdown('<div class="report-section">', unsafe_allow_html=True)
            st.markdown(st.session_state.report)
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Show raw markdown in expander
        with st.expander("📝 View Raw Markdown"):
            st.code(st.session_state.report, language="markdown")

if __name__ == "__main__":
    main()
