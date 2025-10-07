"""
ReAct Agent Framework - Framework for creating agents with reasoning and acting
Multi-provider support: OpenAI, Anthropic, Google, Ollama
"""

__version__ = "0.3.0"
__author__ = "Marcos"
__description__ = "Generic framework for creating AI agent applications using ReAct pattern with multi-provider support"

from react_agent_framework.core.react_agent import ReactAgent
from react_agent_framework.providers import (
    BaseLLMProvider,
    OpenAIProvider,
    AnthropicProvider,
    GoogleProvider,
    OllamaProvider,
)

__all__ = [
    "ReactAgent",
    "BaseLLMProvider",
    "OpenAIProvider",
    "AnthropicProvider",
    "GoogleProvider",
    "OllamaProvider",
]
