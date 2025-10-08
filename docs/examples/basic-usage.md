# Basic Usage Examples

This page provides practical examples to get you started with the ReAct Agent Framework. Each example is self-contained and demonstrates a specific use case.

## Quick Start

The simplest possible agent:

```python
from react_agent_framework import ReactAgent

# Create agent
agent = ReactAgent(
    name="Simple Assistant",
    provider="gpt-4o-mini"
)

# Add a tool
@agent.tool()
def calculate(expression: str) -> str:
    """Perform mathematical calculations"""
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}"

# Run agent
answer = agent.run("What is 15% of 340?")
print(answer)  # Output: 15% of 340 is 51
```

## Example 1: Web Research Assistant

An agent that can search the web and answer questions:

```python
from react_agent_framework import ReactAgent
from duckduckgo_search import DDGS

# Create research agent
agent = ReactAgent(
    name="Research Assistant",
    provider="gpt-4o-mini",
    instructions="You are a helpful research assistant. Provide accurate, well-researched answers."
)

@agent.tool()
def search(query: str) -> str:
    """Search the internet for information"""
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=3))

        if not results:
            return "No results found."

        formatted = []
        for i, result in enumerate(results, 1):
            formatted.append(
                f"{i}. {result['title']}\n   {result['body']}\n   Source: {result['href']}"
            )

        return "\n\n".join(formatted)
    except Exception as e:
        return f"Search error: {str(e)}"

# Use the agent
questions = [
    "What are the latest trends in AI agents?",
    "How does the ReAct pattern work?",
    "What is Python used for?"
]

for question in questions:
    print(f"\nQuestion: {question}")
    answer = agent.run(question, verbose=True)
    print(f"Answer: {answer}\n")
    print("-" * 80)
```

## Example 2: Data Analysis Agent

An agent that can perform calculations and analyze data:

```python
from react_agent_framework import ReactAgent
import json

agent = ReactAgent(
    name="Data Analyst",
    provider="gpt-4o-mini",
    instructions="""You are a data analyst.
    - Always verify your calculations
    - Provide specific numbers and percentages
    - Explain your reasoning"""
)

@agent.tool()
def calculate(expression: str) -> str:
    """Perform mathematical calculations"""
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

@agent.tool()
def get_sales_data() -> str:
    """Get sample sales data"""
    data = {
        "Q1": 125000,
        "Q2": 148000,
        "Q3": 132000,
        "Q4": 175000
    }
    return json.dumps(data)

# Analyze data
questions = [
    "What were the total sales for the year?",
    "Which quarter had the highest sales?",
    "What was the percentage growth from Q1 to Q4?",
    "What was the average quarterly sales?"
]

for question in questions:
    print(f"\n📊 {question}")
    answer = agent.run(question, verbose=True)
    print(f"✅ {answer}\n")
```

## Example 3: File Management Agent

An agent that can interact with the file system:

```python
from react_agent_framework import ReactAgent
import os
import json

agent = ReactAgent(
    name="File Manager",
    provider="gpt-4o-mini",
    instructions="Help users manage and organize their files safely."
)

@agent.tool()
def list_files(directory: str = ".") -> str:
    """List files in a directory"""
    try:
        files = os.listdir(directory)
        return f"Files in {directory}:\n" + "\n".join(f"  - {f}" for f in files)
    except Exception as e:
        return f"Error: {str(e)}"

@agent.tool()
def read_file(filepath: str) -> str:
    """Read contents of a file"""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        return f"Content of {filepath}:\n{content}"
    except Exception as e:
        return f"Error: {str(e)}"

@agent.tool()
def create_file(filepath: str, content: str) -> str:
    """Create a new file with content"""
    try:
        with open(filepath, 'w') as f:
            f.write(content)
        return f"✅ Created {filepath}"
    except Exception as e:
        return f"Error: {str(e)}"

# Use the agent
tasks = [
    "List all files in the current directory",
    "Create a file called 'notes.txt' with the content 'Meeting notes for today'",
    "Read the contents of notes.txt"
]

for task in tasks:
    print(f"\n🔧 Task: {task}")
    result = agent.run(task)
    print(f"✅ {result}\n")
```

## Example 4: Multi-Tool Agent

An agent with multiple capabilities:

```python
from react_agent_framework import ReactAgent
from datetime import datetime
import random

agent = ReactAgent(
    name="Multi-Purpose Assistant",
    provider="gpt-4o-mini",
    max_iterations=15
)

@agent.tool()
def get_current_time() -> str:
    """Get the current time"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@agent.tool()
def calculate(expression: str) -> str:
    """Perform calculations"""
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

@agent.tool()
def generate_random_number(min_val: int = 1, max_val: int = 100) -> str:
    """Generate a random number between min and max"""
    return str(random.randint(min_val, max_val))

@agent.tool()
def get_day_of_week(date_str: str) -> str:
    """Get day of week for a date (format: YYYY-MM-DD)"""
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        return date.strftime("%A")
    except Exception as e:
        return f"Error: {str(e)}"

# Complex queries
queries = [
    "What time is it right now?",
    "Calculate 25 * 48 + 130",
    "Generate a random number between 1 and 50",
    "What day of the week was 2024-01-01?"
]

for query in queries:
    print(f"\n❓ {query}")
    answer = agent.run(query, verbose=True)
    print(f"💡 {answer}\n")
```

## Example 5: Agent with Memory

An agent that remembers previous conversations:

```python
from react_agent_framework import ReactAgent
from react_agent_framework.core.memory import SimpleMemory

# Create agent with memory
agent = ReactAgent(
    name="Personal Assistant",
    provider="gpt-4o-mini",
    memory=SimpleMemory(),
    instructions="Remember what the user tells you and use that context in future responses."
)

@agent.tool()
def set_reminder(task: str) -> str:
    """Set a reminder for a task"""
    return f"✅ Reminder set: {task}"

@agent.tool()
def search(query: str) -> str:
    """Search for information"""
    return f"Search results for: {query}"

# Conversation with context
print("Conversation 1:")
response1 = agent.run("My name is Alice and I love Python programming")
print(response1)

print("\nConversation 2:")
response2 = agent.run("What's my name?")
print(response2)  # Agent remembers: "Alice"

print("\nConversation 3:")
response3 = agent.run("What programming language do I like?")
print(response3)  # Agent remembers: "Python"

print("\nConversation 4:")
response4 = agent.run("Set a reminder to study Python tomorrow")
print(response4)
```

## Example 6: Agent with Objectives

An agent working towards specific goals:

```python
from react_agent_framework import ReactAgent, Objective

# Define objectives
objectives = [
    Objective(
        goal="Gather company information",
        priority="critical",
        success_criteria=["Get company name", "Get revenue data"]
    ),
    Objective(
        goal="Calculate growth metrics",
        priority="high",
        success_criteria=["Calculate YoY growth"]
    ),
    Objective(
        goal="Provide recommendation",
        priority="medium",
        success_criteria=["Analyze data", "Make recommendation"]
    )
]

agent = ReactAgent(
    name="Business Analyst",
    provider="gpt-4o-mini",
    objectives=objectives,
    instructions="Work through objectives systematically."
)

@agent.tool()
def get_company_data(company: str) -> str:
    """Get company financial data"""
    data = {
        "TechCorp": {"revenue_2023": 500000, "revenue_2024": 650000},
        "DataInc": {"revenue_2023": 300000, "revenue_2024": 420000}
    }
    return str(data.get(company, "Company not found"))

@agent.tool()
def calculate(expression: str) -> str:
    """Perform calculations"""
    try:
        return str(eval(expression, {"__builtins__": {}}, {}))
    except Exception as e:
        return f"Error: {str(e)}"

# Agent works towards objectives
answer = agent.run(
    "Analyze TechCorp's financial performance and provide investment recommendation",
    verbose=True
)

print(f"\n📊 Analysis Result:\n{answer}\n")

# Check objective completion
print("\n✅ Objectives Status:")
for obj in agent.objective_tracker.objectives:
    print(f"  - {obj.goal}: {obj.status}")
```

## Example 7: Verbose Mode for Debugging

See agent's reasoning process:

```python
from react_agent_framework import ReactAgent

agent = ReactAgent(
    name="Debug Agent",
    provider="gpt-4o-mini"
)

@agent.tool()
def search(query: str) -> str:
    """Search tool"""
    return f"Results: Found information about {query}"

@agent.tool()
def calculate(expression: str) -> str:
    """Calculate"""
    return str(eval(expression, {"__builtins__": {}}, {}))

# Run with verbose=True to see reasoning
print("=" * 80)
print("VERBOSE MODE - See Agent Thinking")
print("=" * 80)

answer = agent.run(
    "Search for Python tutorials and calculate 10 + 20",
    verbose=True  # Shows Thought → Action → Observation
)

print("=" * 80)
print(f"Final Answer: {answer}")
print("=" * 80)
```

**Output:**
```
================================================================================
VERBOSE MODE - See Agent Thinking
================================================================================

=== Iteration 1 ===
Thought: I need to search for Python tutorials first
Action: search
Action Input: Python tutorials
Observation: Results: Found information about Python tutorials

=== Iteration 2 ===
Thought: Now I need to calculate 10 + 20
Action: calculate
Action Input: 10 + 20
Observation: 30

=== Iteration 3 ===
Thought: I have both pieces of information now
Action: finish
Action Input: Found Python tutorials and 10 + 20 = 30

================================================================================
Final Answer: Found Python tutorials and 10 + 20 = 30
================================================================================
```

## Example 8: Using Built-in Tools

Use framework's built-in tools:

```python
from react_agent_framework import ReactAgent

agent = ReactAgent(
    name="Assistant with Built-in Tools",
    provider="gpt-4o-mini"
)

# Register built-in tools
agent.use_tools("search.duckduckgo")  # Web search
agent.use_tools("filesystem.read")     # Read files
agent.use_tools("compute.calculate")   # Math

# Agent can now use these tools
answer = agent.run(
    "Search for 'Python ReAct agents' and calculate 25 * 4",
    verbose=True
)

print(answer)
```

## Example 9: Multi-Provider Setup

Use different LLM providers:

```python
from react_agent_framework import ReactAgent

# OpenAI (default)
agent_openai = ReactAgent(
    name="OpenAI Agent",
    provider="gpt-4o-mini"
)

# Anthropic Claude
agent_claude = ReactAgent(
    name="Claude Agent",
    provider="anthropic://claude-3-5-sonnet-20241022"
)

# Google Gemini
agent_gemini = ReactAgent(
    name="Gemini Agent",
    provider="google://gemini-1.5-flash"
)

# Ollama (local)
agent_ollama = ReactAgent(
    name="Llama Agent",
    provider="ollama://llama3.2"
)

# Add tools to each
for agent in [agent_openai, agent_claude, agent_gemini, agent_ollama]:
    @agent.tool()
    def greet(name: str) -> str:
        return f"Hello, {name}!"

# Compare responses
question = "Greet me using my name 'Alex'"

print("\nOpenAI:", agent_openai.run(question))
print("\nClaude:", agent_claude.run(question))
print("\nGemini:", agent_gemini.run(question))
print("\nLlama:", agent_ollama.run(question))
```

## Example 10: Temperature Control

Control response creativity:

```python
from react_agent_framework import ReactAgent

# Deterministic (temperature=0)
agent_precise = ReactAgent(
    name="Precise Agent",
    provider="gpt-4o-mini",
    temperature=0  # Same output every time
)

# Creative (temperature=0.7)
agent_creative = ReactAgent(
    name="Creative Agent",
    provider="gpt-4o-mini",
    temperature=0.7  # Varied outputs
)

@agent_precise.tool()
@agent_creative.tool()
def get_info() -> str:
    return "The sky is blue"

question = "Tell me about the sky"

print("Precise agent (run 3 times):")
for i in range(3):
    print(f"  {i+1}. {agent_precise.run(question)}")

print("\nCreative agent (run 3 times):")
for i in range(3):
    print(f"  {i+1}. {agent_creative.run(question)}")
```

## Common Patterns

### Pattern 1: Error Handling in Tools

```python
@agent.tool()
def safe_divide(a: float, b: float) -> str:
    """Safely divide two numbers"""
    try:
        if b == 0:
            return "Error: Division by zero"
        result = a / b
        return f"{a} / {b} = {result}"
    except Exception as e:
        return f"Error: {str(e)}"
```

### Pattern 2: Stateful Tools

```python
class Counter:
    def __init__(self):
        self.count = 0

counter = Counter()

@agent.tool()
def increment() -> str:
    """Increment counter"""
    counter.count += 1
    return f"Counter: {counter.count}"

@agent.tool()
def get_count() -> str:
    """Get current count"""
    return f"Counter: {counter.count}"
```

### Pattern 3: Tool with Multiple Parameters

```python
@agent.tool()
def send_email(to: str, subject: str, body: str) -> str:
    """Send an email"""
    # Email logic here
    return f"✅ Email sent to {to} with subject '{subject}'"
```

### Pattern 4: Tool Returning Structured Data

```python
import json

@agent.tool()
def get_user_info(user_id: int) -> str:
    """Get user information"""
    user = {
        "id": user_id,
        "name": "John Doe",
        "email": "john@example.com",
        "age": 30
    }
    return json.dumps(user, indent=2)
```

## Next Steps

- [Custom Tools](../guides/custom-tools.md) - Create advanced custom tools
- [Memory Systems](../features/memory-systems.md) - Add persistent memory
- [Objectives](../features/objectives.md) - Goal-oriented agents
- [Custom Providers](../guides/custom-providers.md) - Use different LLMs

## Tips and Tricks

### Tip 1: Clear History Between Queries

```python
agent.run("First question")
agent.clear_history()  # Start fresh
agent.run("Unrelated question")
```

### Tip 2: Check Available Tools

```python
tools = agent.get_tools()
print(f"Agent has {len(tools)} tools:")
for name, func in tools.items():
    print(f"  - {name}: {func.__doc__}")
```

### Tip 3: Get Provider Information

```python
info = agent.get_provider_info()
print(f"Provider: {info['provider']}")
print(f"Model: {info['model']}")
```

### Tip 4: Set Max Iterations

```python
# For simple tasks
agent_quick = ReactAgent(max_iterations=5)

# For complex tasks
agent_thorough = ReactAgent(max_iterations=20)
```

## Troubleshooting

### Issue: Agent doesn't use tools

**Solution:** Make sure tool docstrings are clear:

```python
# ❌ Bad: No docstring
@agent.tool()
def search(q):
    return results

# ✅ Good: Clear docstring
@agent.tool()
def search(query: str) -> str:
    """Search the internet for information about the query"""
    return results
```

### Issue: Agent hits max iterations

**Solution:** Increase max_iterations or improve instructions:

```python
agent = ReactAgent(
    max_iterations=20,  # Increase limit
    instructions="Break complex tasks into steps. Use available tools efficiently."
)
```

### Issue: Tool errors aren't handled

**Solution:** Add try-except in tools:

```python
@agent.tool()
def risky_operation(data: str) -> str:
    """Perform risky operation"""
    try:
        result = process(data)
        return f"Success: {result}"
    except Exception as e:
        return f"Error: {str(e)}"  # Return error message
```
