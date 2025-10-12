# ReAct Agent Framework

<p align="center">
  <strong>Complete AI agent framework with MCP support, environments, reasoning strategies, objectives, memory, and built-in tools</strong>
</p>

<p align="center">
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python 3.8+"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://github.com/marcosf63/react-agent-framework"><img src="https://img.shields.io/badge/version-0.9.0-green.svg" alt="Version"></a>
</p>

<p align="center">
  <a href="getting-started/installation/" class="md-button md-button--primary">Getting Started</a>
  <a href="https://github.com/marcosf63/react-agent-framework" class="md-button">View on GitHub</a>
</p>

---

## What is ReAct?

**ReAct** (Reasoning + Acting) is a powerful agent pattern that combines:

- 💭 **Thought (Reasoning)**: Think about what to do next
- ⚡ **Action (Acting)**: Execute actions using available tools
- 👁️ **Observation**: Analyze the results and learn

This cycle continues until the agent has enough information to provide a complete answer.

---

## :sparkles: Key Features

<div class="grid cards" markdown>

-   :material-cloud-outline: __Multi-Provider Support__

    ---

    Support for OpenAI, Anthropic, Google Gemini, and Ollama

    ```python
    agent = ReactAgent(provider="anthropic://claude-3-5-sonnet")
    ```

-   :material-tools: __Built-in Tools__

    ---

    Search, filesystem, computation, and more

    ```python
    agent.use_tools("search.*", "filesystem.*")
    ```

-   :material-brain: __Memory Systems__

    ---

    Simple, ChromaDB, and FAISS memory backends

    ```python
    agent = ReactAgent(memory=ChromaMemory())
    ```

-   :material-target: __Objectives System__

    ---

    Goal-oriented agent management with tracking

    ```python
    agent.objectives.add(Objective(goal="Complete task"))
    ```

-   :material-thought-bubble: __Reasoning Strategies__

    ---

    ReAct, ReWOO, Reflection, and Plan-Execute

    ```python
    reasoning = ReActReasoning(agent, tools)
    ```

-   :material-application-outline: __Environment Interaction__

    ---

    Web, CLI, and filesystem environments

    ```python
    env = WebEnvironment()
    env.step(Action("navigate", {"url": "..."}))
    ```

-   :material-connection: __MCP Integration__

    ---

    Connect to Model Context Protocol servers

    ```python
    agent.add_mcp_server("npx", ["-y", "@mcp/server-filesystem"])
    ```

-   :material-api: __FastAPI-Style API__

    ---

    Elegant and intuitive agent creation

    ```python
    @agent.tool()
    def search(query: str) -> str:
        return results
    ```

</div>

---

## :rocket: Quick Start

### Installation

```bash
pip install react-agent-framework
```

### Your First Agent

```python
from react_agent_framework import ReactAgent

# Create an agent
agent = ReactAgent(
    name="Assistant",
    description="A helpful AI assistant",
    provider="gpt-4o-mini"
)

# Add tools with decorators
@agent.tool()
def search(query: str) -> str:
    """Search the internet for information"""
    # Your search implementation
    return search_results

# Run the agent
answer = agent.run("What is the capital of France?")
print(answer)  # "The capital of France is Paris"
```

That's it! You've created your first ReAct agent. :tada:

---

## :bulb: Why ReAct Agent Framework?

### :zap: Simple and Powerful

Clean, FastAPI-inspired API that makes building agents a breeze:

```python
agent = ReactAgent(name="Research Agent")

@agent.tool()
def search(query: str) -> str:
    """Search for information"""
    return results

answer = agent.run("Research quantum computing")
```

### :electric_plug: Plug and Play

Switch between AI providers with a single line:

=== "OpenAI"
    ```python
    agent = ReactAgent(provider="gpt-4o-mini")
    ```

=== "Anthropic"
    ```python
    agent = ReactAgent(provider="anthropic://claude-3-5-sonnet")
    ```

=== "Google"
    ```python
    agent = ReactAgent(provider="google://gemini-1.5-flash")
    ```

=== "Ollama"
    ```python
    agent = ReactAgent(provider="ollama://llama3.2")
    ```

### :package: Batteries Included

Built-in tools for common tasks:

```python
# Use all search tools
agent.use_tools("search.*")

# Use filesystem tools
agent.use_tools("filesystem.read", "filesystem.write")

# Use computation tools
agent.use_tools("computation.calculator")

# Or use everything
agent.use_tools("*")
```

### :brain: Advanced Memory

Multiple memory backends for context retention:

```python
from react_agent_framework.core.memory import ChromaMemory, FAISSMemory

# Vector-based memory with ChromaDB
agent = ReactAgent(memory=ChromaMemory(collection_name="my_agent"))

# Or FAISS for high-performance similarity search
agent = ReactAgent(memory=FAISSMemory(dimension=1536))
```

### :dart: Goal-Oriented

Track and pursue objectives:

```python
from react_agent_framework.core.objectives import Objective, Priority

agent.objectives.add(Objective(
    goal="Research climate change solutions",
    priority=Priority.HIGH,
    success_criteria=["Find 5 viable solutions", "Analyze feasibility"]
))

# Agent keeps objectives in mind while working
answer = agent.run("Help me with climate research")
```

### :thought_balloon: Multiple Reasoning Strategies

Choose how your agent thinks:

```python
from react_agent_framework.core.reasoning import (
    ReActReasoning,      # Iterative thought-action-observation
    ReWOOReasoning,      # Plan all actions upfront
    ReflectionReasoning, # Self-critique and improve
    PlanExecuteReasoning # Adaptive planning
)

reasoning = ReActReasoning(agent, tools)
result = reasoning.reason("Complex problem to solve")
```

### :desktop_computer: Environment Interaction

Agents can interact with different environments:

```python
from react_agent_framework.core.environment import (
    WebEnvironment,   # Browser automation
    CLIEnvironment,   # Shell commands
    FileEnvironment   # File operations
)

# Web browsing
web_env = WebEnvironment()
web_env.step(Action("navigate", {"url": "https://example.com"}))

# Safe shell execution
cli_env = CLIEnvironment(safe_mode=True)
cli_env.step(Action("execute", {"command": "ls -la"}))
```

### :link: MCP Integration

Connect to external tool servers:

```python
# Connect to filesystem MCP server
agent.add_mcp_server(
    command="npx",
    args=["-y", "@modelcontextprotocol/server-filesystem", "/tmp"],
    name="filesystem"
)

# Connect to GitHub MCP server
agent.add_mcp_server(
    command="npx",
    args=["-y", "@modelcontextprotocol/server-github"],
    env={"GITHUB_TOKEN": "ghp_..."},
    name="github"
)

# All MCP tools are automatically available!
```

---

## :books: Learn More

<div class="grid cards" markdown>

-   :material-clock-fast: __5-Minute Quickstart__

    ---

    Get up and running in minutes

    [:octicons-arrow-right-24: Quickstart](getting-started/quickstart.md)

-   :material-book-open-variant: __Feature Guides__

    ---

    Deep dive into all features

    [:octicons-arrow-right-24: Features](features/multi-provider.md)

-   :material-code-braces: __API Reference__

    ---

    Complete API documentation

    [:octicons-arrow-right-24: API](api-reference/react-agent.md)

-   :material-lightbulb-on: __Examples__

    ---

    Real-world usage examples

    [:octicons-arrow-right-24: Examples](examples/basic-usage.md)

-   :material-robot: __LLMs.txt__

    ---

    Complete documentation for LLM consumption (800+ lines)

    [:octicons-arrow-right-24: LLMs.txt](https://github.com/marcosf63/react-agent-framework/blob/main/LLMs.txt)

</div>

---

## :handshake: Community

- :material-github: [GitHub Repository](https://github.com/marcosf63/react-agent-framework)
- :material-bug: [Report Issues](https://github.com/marcosf63/react-agent-framework/issues)
- :material-email: [Contact](mailto:marcosf63@gmail.com)

---

## :memo: License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/marcosf63/react-agent-framework/blob/main/LICENSE) file for details.

---

<p align="center">
  <strong>Built with :heart: using ReAct Agent Framework</strong>
</p>

<p align="center">
  <a href="getting-started/installation/" class="md-button md-button--primary">Get Started Now</a>
</p>
