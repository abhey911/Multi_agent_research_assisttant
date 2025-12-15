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
        
        # Free API keys with high limits
        self.groq_api_key = os.getenv("GROQ_API_KEY")  # 14,400 requests/day free
        self.openrouter_api_key = os.getenv("OPENROUTER_API_KEY")  # Free tier available
        self.together_api_key = os.getenv("TOGETHER_API_KEY")  # $25 free credit
        
        # Model configuration
        self.gemini_model_flash = os.getenv("GEMINI_MODEL_FLASH", "gemini-2.0-flash")
        self.gemini_model_pro = os.getenv("GEMINI_MODEL_PRO", "gemini-2.5-pro")
        self.groq_model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")  # Fast and free
        self.openrouter_model = os.getenv("OPENROUTER_MODEL", "meta-llama/llama-3.1-8b-instruct:free")
        self.together_model = os.getenv("TOGETHER_MODEL", "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo")
        
        self.hf_model = os.getenv("HF_MODEL", "huggingface/meta-llama/Llama-2-70b-chat-hf")
        self.use_huggingface = os.getenv("USE_HUGGINGFACE", "false").lower() == "true"
        
        # Provider priority: groq > openrouter > together > google
        self.primary_provider = os.getenv("PRIMARY_PROVIDER", "groq")  # Default to Groq (fastest + highest free limit)
        self.max_search_results = int(os.getenv("MAX_SEARCH_RESULTS", 3))
        self.max_iterations = int(os.getenv("MAX_ITERATIONS", 2))
        self.research_depth = os.getenv("RESEARCH_DEPTH", "standard")
        self.request_delay = float(os.getenv("REQUEST_DELAY", 2.0))  # Delay between API calls
        self.max_retries = int(os.getenv("MAX_RETRIES", 3))
        
        # Set API keys as environment variables
        if self.google_api_key:
            os.environ["GOOGLE_API_KEY"] = self.google_api_key
        if self.huggingface_api_key:
            os.environ["HUGGINGFACE_API_KEY"] = self.huggingface_api_key
    
    def validate(self):
        """Validate that at least one API key is configured."""
        has_provider = any([
            self.groq_api_key,
            self.openrouter_api_key,
            self.together_api_key,
            self.google_api_key,
            (self.use_huggingface and self.huggingface_api_key)
        ])
        
        if not has_provider:
            raise ValueError(
                "No API key configured. Please set at least one of: \n"
                "- GROQ_API_KEY (recommended - 14,400 free requests/day)\n"
                "- OPENROUTER_API_KEY (free tier available)\n"
                "- TOGETHER_API_KEY ($25 free credit)\n"
                "- GOOGLE_API_KEY (Gemini)"
            )
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
