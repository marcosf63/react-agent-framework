"""
Pytest configuration and shared fixtures
"""

import pytest
from unittest.mock import Mock, MagicMock, patch
from typing import List


@pytest.fixture
def mock_llm_response():
    """Mock LLM response for testing agent execution"""
    return """Thought: I need to use the test_tool
Action: test_tool
Action Input: test input
Observation: Tool executed successfully
Thought: I have the answer
Action: finish
Action Input: Final answer based on the tool result"""


@pytest.fixture
def mock_openai_provider():
    """Mock OpenAI provider that returns predictable responses"""
    provider = Mock()
    provider.generate.return_value = "Mocked LLM response"
    provider.get_model_name.return_value = "gpt-4o-mini"
    return provider


@pytest.fixture
def mock_anthropic_provider():
    """Mock Anthropic provider"""
    provider = Mock()
    provider.generate.return_value = "Mocked Claude response"
    provider.get_model_name.return_value = "claude-3-5-sonnet-20241022"
    return provider


@pytest.fixture
def mock_ollama_provider():
    """Mock Ollama provider"""
    provider = Mock()
    provider.generate.return_value = "Mocked Ollama response"
    provider.get_model_name.return_value = "llama3.2"
    return provider


@pytest.fixture
def simple_agent(mock_openai_provider):
    """Create a simple agent for testing"""
    from react_agent_framework import ReactAgent

    agent = ReactAgent(
        name="Test Agent",
        description="Agent for testing",
        provider=mock_openai_provider
    )
    return agent


@pytest.fixture
def agent_with_tool(simple_agent):
    """Agent with a registered test tool"""
    @simple_agent.tool()
    def test_tool(input_text: str) -> str:
        """A test tool that echoes input"""
        return f"Echo: {input_text}"

    return simple_agent


@pytest.fixture
def sample_messages():
    """Sample messages for memory testing"""
    return [
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hi there!"},
        {"role": "user", "content": "How are you?"},
        {"role": "assistant", "content": "I'm doing well, thanks!"},
    ]


@pytest.fixture
def sample_objectives():
    """Sample objectives for testing"""
    from react_agent_framework import Objective

    return [
        Objective(
            goal="Complete task 1",
            priority="critical",
            success_criteria=["Criteria 1", "Criteria 2"]
        ),
        Objective(
            goal="Complete task 2",
            priority="high",
            success_criteria=["Criteria A"]
        ),
        Objective(
            goal="Complete task 3",
            priority="medium",
            success_criteria=["Criteria X", "Criteria Y"]
        ),
    ]


@pytest.fixture(autouse=True)
def reset_environment():
    """Reset environment between tests"""
    yield
    # Cleanup code if needed
