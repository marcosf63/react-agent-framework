# Quickstart

Get up and running with ReAct Agent Framework in 5 minutes!

---

## Step 1: Install

```bash
pip install react-agent-framework
```

---

## Step 2: Configure API Key

Create a `.env` file:

```env
OPENAI_API_KEY=sk-your-key-here
```

---

## Step 3: Create Your First Agent

Create a file `my_agent.py`:

```python
from react_agent_framework import ReactAgent

# Create agent
agent = ReactAgent(
    name="Assistant",
    description="A helpful AI assistant"
)

# Add a simple tool
@agent.tool()
def greet(name: str) -> str:
    """Greet someone by name"""
    return f"Hello, {name}! Nice to meet you!"

# Run the agent
answer = agent.run("Greet Alice")
print(answer)
```

---

## Step 4: Run It

```bash
python my_agent.py
```

Output:
```
Hello, Alice! Nice to meet you!
```

---

## Step 5: Add More Tools

```python
from react_agent_framework import ReactAgent

agent = ReactAgent(name="Calculator Agent")

@agent.tool()
def add(a: float, b: float) -> str:
    """Add two numbers"""
    return f"{a} + {b} = {a + b}"

@agent.tool()
def multiply(a: float, b: float) -> str:
    """Multiply two numbers"""
    return f"{a} × {b} = {a * b}"

# Agent can now use multiple tools
answer = agent.run("What is 5 plus 3?")
print(answer)  # "8"

answer = agent.run("Multiply 4 by 7")
print(answer)  # "28"
```

---

## Step 6: Use Built-in Tools

```python
from react_agent_framework import ReactAgent

agent = ReactAgent(name="Research Agent")

# Use all search tools
agent.use_tools("search.*")

# Now agent can search the web
answer = agent.run("What is the latest news about AI?")
print(answer)
```

---

## Step 7: Try Different Providers

=== "OpenAI (Default)"
    ```python
    agent = ReactAgent(
        name="GPT Agent",
        provider="gpt-4o-mini"
    )
    ```

=== "Anthropic Claude"
    ```python
    agent = ReactAgent(
        name="Claude Agent",
        provider="anthropic://claude-3-5-sonnet-20241022"
    )
    ```

=== "Google Gemini"
    ```python
    agent = ReactAgent(
        name="Gemini Agent",
        provider="google://gemini-1.5-flash"
    )
    ```

=== "Ollama (Local)"
    ```python
    agent = ReactAgent(
        name="Llama Agent",
        provider="ollama://llama3.2"
    )
    ```

---

## Step 8: Enable Verbose Mode

See the agent's reasoning process:

```python
agent = ReactAgent(name="Debug Agent")

@agent.tool()
def search(query: str) -> str:
    """Search for information"""
    return f"Results for: {query}"

# Enable verbose mode
answer = agent.run(
    "Search for Python programming tips",
    verbose=True  # Shows step-by-step reasoning
)
```

Output:
```
============================================================
ITERATION 1
============================================================

Thought: I need to search for Python programming tips
Action: search
Action Input: Python programming tips

Observation: Results for: Python programming tips

Thought: I have the search results
Action: finish
Action Input: Found Python programming tips

============================================================
Answer: Found Python programming tips
```

---

## Step 9: Add Memory

Make your agent remember conversations:

```python
from react_agent_framework import ReactAgent

agent = ReactAgent(
    name="Memory Agent",
    enable_memory=True  # Simple memory
)

@agent.tool()
def save_note(note: str) -> str:
    """Save a note"""
    return f"Saved: {note}"

# First conversation
agent.run("Save a note: Meeting at 3pm")

# Later conversation - agent remembers context
agent.run("What time is my meeting?")
# Agent can use memory to recall the saved note
```

---

## What's Next?

<div class="grid cards" markdown>

-   :material-robot: __Build Complete Agents__

    ---

    Learn to build sophisticated agents

    [:octicons-arrow-right-24: First Agent Tutorial](first-agent.md)

-   :material-tools: __Explore Built-in Tools__

    ---

    Discover all available tools

    [:octicons-arrow-right-24: Built-in Tools](../features/built-in-tools.md)

-   :material-brain: __Add Memory__

    ---

    Give your agent memory

    [:octicons-arrow-right-24: Memory Systems](../features/memory-systems.md)

-   :material-connection: __Use MCP Servers__

    ---

    Connect to external tools

    [:octicons-arrow-right-24: MCP Integration](../features/mcp-integration.md)

</div>

---

## Common Patterns

### Research Agent

```python
agent = ReactAgent(name="Researcher")
agent.use_tools("search.*")

answer = agent.run("Research quantum computing applications")
```

### File Management Agent

```python
agent = ReactAgent(name="File Manager")
agent.use_tools("filesystem.*")

answer = agent.run("List all Python files in current directory")
```

### Calculator Agent

```python
agent = ReactAgent(name="Calculator")
agent.use_tools("computation.*")

answer = agent.run("Calculate the compound interest on $1000 at 5% for 10 years")
```

### Multi-Tool Agent

```python
agent = ReactAgent(name="Multi-Tool Agent")
agent.use_tools("*")  # All tools

answer = agent.run("Search for Python tutorials and save results to a file")
```

---

!!! success "You're Ready!"
    You now know the basics of ReAct Agent Framework. Explore the [Features](../features/multi-provider.md) section to learn more!
