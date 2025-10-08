# Your First Agent

Build a complete agent step-by-step and learn best practices.

---

## Project Setup

Create a new project directory:

```bash
mkdir my-agent-project
cd my-agent-project
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install react-agent-framework
```

Create `.env` file:

```env
OPENAI_API_KEY=sk-your-key-here
```

---

## Simple Calculator Agent

Let's build a calculator agent that can perform mathematical operations.

### Step 1: Create the Agent

```python title="calculator_agent.py"
from react_agent_framework import ReactAgent

# Create the agent
agent = ReactAgent(
    name="Calculator",
    description="A mathematical calculator assistant",
    provider="gpt-4o-mini",
    temperature=0,  # Deterministic for calculations
    max_iterations=5
)
```

### Step 2: Add Tools

```python
@agent.tool()
def add(a: float, b: float) -> str:
    """Add two numbers together"""
    result = a + b
    return f"{a} + {b} = {result}"

@agent.tool()
def subtract(a: float, b: float) -> str:
    """Subtract b from a"""
    result = a - b
    return f"{a} - {b} = {result}"

@agent.tool()
def multiply(a: float, b: float) -> str:
    """Multiply two numbers"""
    result = a * b
    return f"{a} × {b} = {result}"

@agent.tool()
def divide(a: float, b: float) -> str:
    """Divide a by b"""
    if b == 0:
        return "Error: Cannot divide by zero"
    result = a / b
    return f"{a} ÷ {b} = {result}"
```

### Step 3: Test It

```python
if __name__ == "__main__":
    # Test calculations
    questions = [
        "What is 15 plus 27?",
        "Multiply 8 by 9",
        "What is 100 divided by 4?",
        "Calculate 50 minus 23"
    ]

    for question in questions:
        print(f"\nQ: {question}")
        answer = agent.run(question, verbose=False)
        print(f"A: {answer}")
```

---

## Research Assistant

Build a more advanced agent that can search and analyze information.

```python title="research_agent.py"
from react_agent_framework import ReactAgent

# Create research agent
agent = ReactAgent(
    name="Research Assistant",
    description="An AI that helps with web research and analysis",
    provider="gpt-4o-mini"
)

# Use built-in search tools
agent.use_tools("search.*")

# Add custom analysis tool
@agent.tool()
def summarize(text: str) -> str:
    """Create a brief summary of the given text"""
    # In real implementation, you might use another LLM call or algorithm
    words = text.split()
    summary = " ".join(words[:100])  # Simple truncation
    return f"Summary: {summary}..."

# Use it
question = "What are the latest developments in quantum computing?"
answer = agent.run(question, verbose=True)
print(f"\nFinal Answer: {answer}")
```

---

## File Management Agent

Agent that can work with files and directories.

```python title="file_agent.py"
from react_agent_framework import ReactAgent
from pathlib import Path

agent = ReactAgent(
    name="File Manager",
    description="Helps manage files and directories",
    provider="gpt-4o-mini"
)

# Use filesystem tools
agent.use_tools("filesystem.*")

# Add custom tool
@agent.tool()
def count_files(directory: str) -> str:
    """Count the number of files in a directory"""
    try:
        path = Path(directory)
        files = list(path.glob("*"))
        file_count = len([f for f in files if f.is_file()])
        dir_count = len([f for f in files if f.is_dir()])
        return f"Found {file_count} files and {dir_count} directories in {directory}"
    except Exception as e:
        return f"Error: {str(e)}"

# Use it
tasks = [
    "List all files in the current directory",
    "Count how many Python files are here",
]

for task in tasks:
    print(f"\nTask: {task}")
    result = agent.run(task)
    print(f"Result: {result}")
```

---

## Multi-Purpose Agent

Combine multiple capabilities in one agent.

```python title="multi_agent.py"
from react_agent_framework import ReactAgent

agent = ReactAgent(
    name="Multi-Purpose Assistant",
    description="An assistant that can search, calculate, and manage files",
    provider="gpt-4o-mini",
    enable_memory=True  # Remember conversations
)

# Add all built-in tools
agent.use_tools("*")

# Add custom tools
@agent.tool()
def create_report(title: str, content: str) -> str:
    """Create a formatted report"""
    report = f"""
    ={'='*50}
    REPORT: {title}
    ={'='*50}

    {content}

    ={'='*50}
    """
    return report

# Interactive mode
print("Multi-Purpose Assistant (type 'quit' to exit)")
while True:
    query = input("\nYou: ")
    if query.lower() in ['quit', 'exit', 'bye']:
        break

    answer = agent.run(query)
    print(f"Assistant: {answer}")
```

---

## Best Practices

### 1. Clear Tool Descriptions

```python
@agent.tool()
def search_papers(query: str, year: int = 2024) -> str:
    """
    Search for academic papers.

    Args:
        query: The search query (topic, keywords, etc.)
        year: Publication year to filter by (default: 2024)

    Returns:
        List of relevant papers found
    """
    # Implementation
    pass
```

### 2. Error Handling

```python
@agent.tool()
def divide(a: float, b: float) -> str:
    """Divide two numbers"""
    try:
        if b == 0:
            return "Error: Cannot divide by zero"
        result = a / b
        return f"{a} ÷ {b} = {result}"
    except Exception as e:
        return f"Error performing division: {str(e)}"
```

### 3. Type Hints

```python
from typing import List, Dict, Optional

@agent.tool()
def analyze_data(
    values: List[float],
    method: str = "mean"
) -> str:
    """Analyze a list of numerical values"""
    # Implementation with proper typing
    pass
```

### 4. Appropriate Temperature

```python
# For factual/deterministic tasks
calculator = ReactAgent(
    name="Calculator",
    temperature=0  # No randomness
)

# For creative tasks
writer = ReactAgent(
    name="Writer",
    temperature=0.7  # More creative
)
```

### 5. Iteration Limits

```python
agent = ReactAgent(
    name="Agent",
    max_iterations=10  # Prevent infinite loops
)
```

---

## Next Steps

<div class="grid cards" markdown>

-   :material-cloud: __Try Different Providers__

    ---

    Learn about multi-provider support

    [:octicons-arrow-right-24: Multi-Provider](../features/multi-provider.md)

-   :material-brain: __Add Memory__

    ---

    Give your agent memory

    [:octicons-arrow-right-24: Memory Systems](../features/memory-systems.md)

-   :material-target: __Set Objectives__

    ---

    Make goal-oriented agents

    [:octicons-arrow-right-24: Objectives](../features/objectives.md)

-   :material-connection: __Connect to MCP__

    ---

    Use external tool servers

    [:octicons-arrow-right-24: MCP Integration](../features/mcp-integration.md)

</div>

---

## Complete Example

Here's a complete, production-ready example:

```python title="production_agent.py"
from react_agent_framework import ReactAgent
from react_agent_framework.core.memory import SimpleMemory
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

def create_agent():
    """Factory function to create configured agent"""
    agent = ReactAgent(
        name="Production Assistant",
        description="A production-ready AI assistant",
        provider="gpt-4o-mini",
        temperature=0.3,
        max_iterations=10,
        memory=SimpleMemory(max_messages=100)
    )

    # Add tools
    agent.use_tools("search.*", "computation.*")

    @agent.tool()
    def custom_tool(param: str) -> str:
        """Custom tool with proper error handling"""
        try:
            # Your implementation
            result = f"Processed: {param}"
            return result
        except Exception as e:
            logging.error(f"Tool error: {e}")
            return f"Error: {str(e)}"

    return agent

def main():
    agent = create_agent()

    # Example usage
    result = agent.run(
        "Search for Python best practices and summarize",
        verbose=True
    )

    print(f"\nResult: {result}")

if __name__ == "__main__":
    main()
```

Run it:

```bash
python production_agent.py
```

---

!!! success "Congratulations!"
    You've built your first complete agent! Continue exploring the framework's features to build even more powerful agents.
