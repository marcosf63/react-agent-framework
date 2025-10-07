"""
ReAct Agent Framework - Complete framework for creating intelligent agents

Features:
- Multi-provider support: OpenAI, Anthropic, Google, Ollama
- Built-in tools: Search, Filesystem, Computation
- Memory systems: Simple, ChromaDB, FAISS
- Objectives: Goal-oriented agent management
- Reasoning strategies: ReAct, ReWOO, Reflection, Plan-Execute
- Environments: Web, CLI, File system interaction
"""

__version__ = "0.8.0"
__author__ = "Marcos"
__description__ = "Complete AI agent framework with environments, multiple reasoning strategies, multi-provider support, built-in tools, memory, and objectives"

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
