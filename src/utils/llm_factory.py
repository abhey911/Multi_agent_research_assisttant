"""LLM Factory for creating language models with multiple provider support."""

import os
from typing import Optional
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI


def create_llm(config, temperature: float = 0.5):
    """
    Create LLM instance using available providers in priority order.
    
    Priority: Groq > OpenRouter > Together > Google Gemini
    
    Args:
        config: Configuration object with API keys
        temperature: Model temperature
        
    Returns:
        LLM instance
    """
    provider = config.primary_provider.lower()
    
    # Try providers in priority order
    providers = ['groq', 'openrouter', 'together', 'google']
    if provider in providers:
        providers.remove(provider)
        providers.insert(0, provider)
    
    for prov in providers:
        try:
            if prov == 'groq' and config.groq_api_key:
                print(f"✓ Using Groq ({config.groq_model}) - 14,400 free requests/day")
                return ChatGroq(
                    model=config.groq_model,
                    temperature=temperature,
                    groq_api_key=config.groq_api_key,
                    max_retries=config.max_retries
                )
                
            elif prov == 'openrouter' and config.openrouter_api_key:
                print(f"✓ Using OpenRouter ({config.openrouter_model})")
                return ChatOpenAI(
                    model=config.openrouter_model,
                    temperature=temperature,
                    openai_api_key=config.openrouter_api_key,
                    openai_api_base="https://openrouter.ai/api/v1",
                    max_retries=config.max_retries
                )
                
            elif prov == 'together' and config.together_api_key:
                print(f"✓ Using Together AI ({config.together_model})")
                return ChatOpenAI(
                    model=config.together_model,
                    temperature=temperature,
                    openai_api_key=config.together_api_key,
                    openai_api_base="https://api.together.xyz/v1",
                    max_retries=config.max_retries
                )
                
            elif prov == 'google' and config.google_api_key:
                print(f"✓ Using Google Gemini ({config.gemini_model_flash})")
                return ChatGoogleGenerativeAI(
                    model=config.gemini_model_flash,
                    temperature=temperature,
                    convert_system_message_to_human=True,
                    max_retries=config.max_retries
                )
        except Exception as e:
            print(f"⚠ Failed to initialize {prov}: {str(e)}")
            continue
    
    raise RuntimeError("No working LLM provider available. Please configure API keys.")


def get_available_providers(config) -> list:
    """Get list of available providers based on configured API keys."""
    providers = []
    
    if config.groq_api_key:
        providers.append("Groq (14,400 free req/day)")
    if config.openrouter_api_key:
        providers.append("OpenRouter (free tier)")
    if config.together_api_key:
        providers.append("Together AI ($25 credit)")
    if config.google_api_key:
        providers.append("Google Gemini")
    if config.use_huggingface and config.huggingface_api_key:
        providers.append("HuggingFace")
    
    return providers
