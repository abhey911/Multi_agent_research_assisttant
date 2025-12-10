"""Configuration utilities for the multi-agent research system."""

import os
import yaml
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for the research assistant."""
    
    def __init__(self):
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        self.huggingface_api_key = os.getenv("HUGGINGFACE_API_KEY")
        self.serpapi_api_key = os.getenv("SERPAPI_API_KEY")
        self.gemini_model_flash = os.getenv("GEMINI_MODEL_FLASH", "gemini-2.5-flash")
        self.gemini_model_pro = os.getenv("GEMINI_MODEL_PRO", "gemini-2.5-pro")
        self.hf_model = os.getenv("HF_MODEL", "huggingface/meta-llama/Llama-2-70b-chat-hf")
        self.use_huggingface = os.getenv("USE_HUGGINGFACE", "false").lower() == "true"
        self.max_search_results = int(os.getenv("MAX_SEARCH_RESULTS", 10))
        self.max_iterations = int(os.getenv("MAX_ITERATIONS", 5))
        self.research_depth = os.getenv("RESEARCH_DEPTH", "standard")
        
        # Set API keys as environment variables
        if self.google_api_key:
            os.environ["GOOGLE_API_KEY"] = self.google_api_key
        if self.huggingface_api_key:
            os.environ["HUGGINGFACE_API_KEY"] = self.huggingface_api_key
    
    def validate(self):
        """Validate that required configuration is present."""
        if not self.use_huggingface and not self.google_api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables")
        if self.use_huggingface and not self.huggingface_api_key:
            raise ValueError("HUGGINGFACE_API_KEY not found in environment variables when USE_HUGGINGFACE is true")
        return True

def load_config():
    """Load and return configuration object."""
    config = Config()
    config.validate()
    return config

def get_agent_config(config_path=None):
    """Load agent configuration from YAML file."""
    if config_path is None:
        # Get the project root directory
        current_dir = Path(__file__).parent.parent.parent
        config_path = current_dir / "config" / "agents_config.yaml"
    
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    return config.get('agents', {})

def get_task_config(config_path=None):
    """Load task configuration from YAML file."""
    if config_path is None:
        # Get the project root directory
        current_dir = Path(__file__).parent.parent.parent
        config_path = current_dir / "config" / "agents_config.yaml"
    
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    return config.get('tasks', {})
