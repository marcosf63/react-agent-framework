# Built-in Tools

ReAct Agent Framework comes with a rich set of built-in tools that agents can use out of the box.

---

## Overview

Built-in tools are organized into categories and can be registered using pattern matching:

```python
from react_agent_framework import ReactAgent

agent = ReactAgent(name="Assistant")

# Register specific tool
agent.use_tools("search.duckduckgo")

# Register all tools in a category
agent.use_tools("filesystem.*")

# Register all available tools
agent.use_tools("*")
```

---

## Available Tools

### :mag: Search Tools

Search the web for information using DuckDuckGo.

#### `search.duckduckgo`

Search the internet for current information.

**Example**:

```python
from react_agent_framework import ReactAgent

agent = ReactAgent(
    name="Research Assistant",
    provider="gpt-4o-mini"
)

# Register search tool
agent.use_tools("search.duckduckgo")

# Agent can now search the web
answer = agent.run("What is the latest version of Python?", verbose=True)
print(answer)
```

**Output**:
```
============================================================
ITERATION 1
============================================================

Thought: I need to search for the latest Python version
Action: search_duckduckgo
Action Input: latest Python version 2024

Observation: Python 3.12 is the latest stable version...

Thought: I have the information
Action: finish
Action Input: The latest version of Python is 3.12

============================================================
Answer: The latest version of Python is 3.12
```

---

### :file_folder: Filesystem Tools

Interact with the local filesystem safely.

#### `filesystem.read`

Read contents of a file.

#### `filesystem.write`

Write content to a file.

#### `filesystem.list`

List files in a directory.

#### `filesystem.delete`

Delete a file (use with caution!).

**Example**:

```python
from react_agent_framework import ReactAgent

agent = ReactAgent(
    name="File Assistant",
    provider="gpt-4o-mini"
)

# Register all filesystem tools
agent.use_tools("filesystem.*")

# List Python files
answer = agent.run("List all Python files in the current directory")
print(answer)
```

**Example Output**:
```
Found 5 Python files:
- main.py
- agent.py
- tools.py
- config.py
- __init__.py
```

**Read and Write Example**:

```python
agent = ReactAgent(name="File Manager")
agent.use_tools("filesystem.read", "filesystem.write")

# Read a file
answer = agent.run("Read the contents of README.md")

# Write to a file
answer = agent.run("Write 'Hello World' to test.txt")
```

!!! warning "Safety"
    Filesystem tools have built-in safety features:

    - Cannot delete system files
    - Cannot modify protected directories
    - Requires confirmation for destructive operations

---

### :abacus: Computation Tools

Perform calculations and execute code safely.

#### `computation.calculator`

Evaluate mathematical expressions.

#### `computation.code_executor`

Execute Python code safely (sandboxed).

#### `computation.shell`

Execute shell commands (with restrictions).

**Calculator Example**:

```python
from react_agent_framework import ReactAgent

agent = ReactAgent(
    name="Math Assistant",
    provider="gpt-4o-mini",
    temperature=0  # Deterministic for calculations
)

# Register calculator
agent.use_tools("computation.calculator")

# Perform calculations
answer = agent.run("What is 25 * 4 + 100 / 2?")
print(answer)  # "150"
```

**Complex Calculation**:

```python
agent = ReactAgent(name="Calculator")
agent.use_tools("computation.calculator")

answer = agent.run("""
Calculate the compound interest for:
- Principal: $1000
- Rate: 5% per year
- Time: 10 years
- Compounded annually

Use the formula: A = P(1 + r)^t
""")

print(answer)  # Approximately $1628.89
```

---

## Pattern Matching

Use glob-style patterns to register multiple tools:

### Register All Tools in Category

```python
# All search tools
agent.use_tools("search.*")

# All filesystem tools
agent.use_tools("filesystem.*")

# All computation tools
agent.use_tools("computation.*")
```

### Register Specific Tools

```python
# Just calculator and file list
agent.use_tools(
    "computation.calculator",
    "filesystem.list"
)
```

### Register Everything

```python
# All available tools
agent.use_tools("*")

# Check what was registered
tools = agent.get_tools()
print(f"Registered {len(tools)} tools:")
for name in tools:
    print(f"  - {name}")
```

---

## Complete Example: Multi-Tool Agent

Combine different tool categories:

```python
from react_agent_framework import ReactAgent

agent = ReactAgent(
    name="Multi-Tool Assistant",
    provider="gpt-4o-mini",
    temperature=0
)

# Register tools from different categories
agent.use_tools(
    "search.duckduckgo",      # Web search
    "computation.calculator",  # Math
    "filesystem.list"          # File operations
)

# Complex task using multiple tools
answer = agent.run("""
1. Search for the current Python version
2. Calculate 2024 - 1991 (Python's birth year)
3. List files in the current directory
""", verbose=True)

print(f"\nFinal Answer:\n{answer}")
```

**Expected Output**:
```
Final Answer:
1. Python 3.12 is the current stable version
2. Python is 33 years old (2024 - 1991 = 33)
3. Found 5 files in current directory: main.py, README.md, ...
```

---

## Tool Registry API

### List Available Tools

```python
from react_agent_framework.tools.registry import ToolRegistry

# Find all tools matching pattern
search_tools = ToolRegistry.find_tools("search.*")
print(f"Found {len(search_tools)} search tools")

# Find all filesystem tools
fs_tools = ToolRegistry.find_tools("filesystem.*")
for tool in fs_tools:
    print(f"- {tool.name}: {tool.description}")
```

### Check Registered Tools

```python
agent = ReactAgent(name="Agent")
agent.use_tools("*")

# Get all registered tools
tools = agent.get_tools()

# Print tool names and descriptions
for name, description in tools.items():
    print(f"{name}:")
    print(f"  {description}\n")
```

---

## Best Practices

### 1. Register Only Needed Tools

```python
# ❌ Bad: Register everything when you only need calculator
agent.use_tools("*")

# ✅ Good: Register only what you need
agent.use_tools("computation.calculator")
```

### 2. Use Appropriate Temperature

```python
# For deterministic tasks (math, file operations)
agent = ReactAgent(
    name="Calculator",
    temperature=0  # No randomness
)

# For creative tasks (research, writing)
agent = ReactAgent(
    name="Researcher",
    temperature=0.7  # More creative
)
```

### 3. Handle Errors Gracefully

```python
agent = ReactAgent(name="File Agent")
agent.use_tools("filesystem.*")

try:
    answer = agent.run("Delete important_file.txt")
except Exception as e:
    print(f"Error: {e}")
```

### 4. Use Verbose Mode for Debugging

```python
# See the agent's reasoning process
answer = agent.run(
    "Calculate 15 * 20",
    verbose=True  # Shows thought-action-observation
)
```

---

## Tool Categories Reference

| Category | Tools | Description |
|----------|-------|-------------|
| **search** | `duckduckgo` | Web search with DuckDuckGo |
| **filesystem** | `read`, `write`, `list`, `delete` | File and directory operations |
| **computation** | `calculator`, `code_executor`, `shell` | Mathematical and code execution |

---

## Next Steps

<div class="grid cards" markdown>

-   :material-wrench: __Create Custom Tools__

    ---

    Learn how to create your own tools

    [:octicons-arrow-right-24: Custom Tools Guide](../guides/custom-tools.md)

-   :material-brain: __Add Memory__

    ---

    Give your agent memory capabilities

    [:octicons-arrow-right-24: Memory Systems](memory-systems.md)

-   :material-connection: __Use MCP Servers__

    ---

    Connect to external tool servers

    [:octicons-arrow-right-24: MCP Integration](mcp-integration.md)

</div>

---

## Examples

For complete, runnable examples, see:

- [builtin_tools.py](https://github.com/marcosf63/react-agent-framework/blob/main/react_agent_framework/examples/builtin_tools.py) - All built-in tools demonstration
- [Basic Usage](../examples/basic-usage.md) - Getting started examples
- [Web Research](../examples/web-research.md) - Research agent example
