# Memory Systems

Give your agents the ability to remember conversations and retrieve relevant context.

---

## Overview

Memory systems allow agents to:

- **Remember** previous conversations
- **Retrieve** relevant information using semantic search
- **Maintain context** across multiple interactions
- **Learn** from past experiences

```python
from react_agent_framework import ReactAgent
from react_agent_framework.core.memory import SimpleMemory

agent = ReactAgent(
    name="Assistant",
    memory=SimpleMemory(max_messages=100)
)
```

---

## Available Memory Backends

| Backend | Type | Best For |
|---------|------|----------|
| **SimpleMemory** | In-memory buffer | Development, simple bots |
| **ChromaMemory** | Vector database | Production, semantic search |
| **FAISSMemory** | High-performance | Large-scale, fast retrieval |

---

## SimpleMemory

In-memory conversation history with keyword matching.

### Basic Usage

```python
from react_agent_framework import ReactAgent
from react_agent_framework.core.memory import SimpleMemory

# Create agent with memory
agent = ReactAgent(
    name="Memory Assistant",
    memory=SimpleMemory(max_messages=50)
)

# Add a tool
@agent.tool()
def calculate(expression: str) -> str:
    """Calculate mathematical expressions"""
    try:
        return f"Result: {eval(expression, {'__builtins__': {}}, {})}"
    except Exception as e:
        return f"Error: {str(e)}"

# Conversation 1
agent.run("My name is Alice")

# Conversation 2 - Agent remembers!
answer = agent.run("What is my name?")
print(answer)  # "Your name is Alice"
```

### Features

✅ **Simple and fast**
✅ **No external dependencies**
✅ **Good for development**
❌ **Limited to keyword matching**
❌ **Lost on restart**

---

## ChromaMemory

Vector database with semantic search capabilities.

### Installation

```bash
pip install react-agent-framework[chroma]
```

### Usage

```python
from react_agent_framework import ReactAgent
from react_agent_framework.core.memory import ChromaMemory

agent = ReactAgent(
    name="Smart Assistant",
    memory=ChromaMemory(
        collection_name="my_agent",
        persist_directory="./chroma_db",
        embedding_function="default"  # or "openai"
    )
)

# Add knowledge to memory
agent.memory.add("Python was created by Guido van Rossum", role="system")
agent.memory.add("Python emphasizes code readability", role="system")

# Semantic search
results = agent.memory.search("programming language design", top_k=2)
for msg in results:
    print(msg.content)
```

### Features

✅ **Semantic search** - Finds related content
✅ **Persistent** - Survives restarts
✅ **Vector similarity** - Better than keywords
✅ **Production-ready**

---

## FAISSMemory

High-performance similarity search for large-scale applications.

### Installation

```bash
pip install react-agent-framework[faiss]
```

### Usage

```python
from react_agent_framework import ReactAgent
from react_agent_framework.core.memory import FAISSMemory

agent = ReactAgent(
    name="Performance Assistant",
    memory=FAISSMemory(
        index_path="./faiss_index",
        dimension=1536,  # OpenAI embedding size
        index_type="Flat"  # or "IVF", "HNSW"
    )
)

# Add technical docs
agent.memory.add("Docker enables application containerization", role="system")
agent.memory.add("Kubernetes orchestrates container deployment", role="system")

# Fast semantic search
results = agent.memory.search("container technology", top_k=2)
```

### Index Types

| Type | Speed | Accuracy | Best For |
|------|-------|----------|----------|
| **Flat** | Slower | 100% | <100K vectors |
| **IVF** | Fast | ~95% | 100K-1M vectors |
| **HNSW** | Very fast | ~98% | >1M vectors |

---

## Memory API

All memory backends implement the same interface:

### add()

Add a message to memory:

```python
# System message
agent.memory.add("Important context", role="system")

# User message
agent.memory.add("User question", role="user")

# Assistant message
agent.memory.add("Assistant answer", role="assistant")
```

### search()

Search for relevant messages:

```python
# Semantic search
results = agent.memory.search(
    query="topic to search",
    top_k=5,  # Return top 5 results
    filter_role="system"  # Optional: filter by role
)

for msg in results:
    print(f"[{msg.role}] {msg.content}")
```

### clear()

Clear all messages:

```python
agent.memory.clear()
```

### get_stats()

Get memory statistics:

```python
stats = agent.memory.get_stats()
print(f"Total messages: {stats['total_messages']}")
print(f"Total tokens: {stats.get('total_tokens', 'N/A')}")
```

---

## Complete Example

Agent that learns from conversations:

```python
from react_agent_framework import ReactAgent
from react_agent_framework.core.memory import ChromaMemory

# Create agent with persistent memory
agent = ReactAgent(
    name="Learning Assistant",
    memory=ChromaMemory(
        collection_name="assistant_memory",
        persist_directory="./memory_db"
    )
)

# Session 1: Teaching
agent.run("Remember: The capital of France is Paris")
agent.run("Remember: Python was created in 1991")

# Session 2: Later (even after restart)
# Memory is persistent!
answer = agent.run("What's the capital of France?")
print(answer)  # "Paris"

answer = agent.run("When was Python created?")
print(answer)  # "1991"
```

---

## Choosing a Memory Backend

### Use SimpleMemory when:

- 🚀 Starting development
- 💻 Building simple chatbots
- 🔧 Testing and prototyping
- ⚡ Don't need persistence

### Use ChromaMemory when:

- 🏢 Building production applications
- 🔍 Need semantic search
- 💾 Need persistence
- 📈 Moderate scale (<1M messages)

### Use FAISSMemory when:

- ⚡ Need maximum performance
- 📊 Large-scale applications (>1M messages)
- 🎯 Accuracy is critical
- 🔬 Research/experimentation

---

## Best Practices

### 1. Initialize Memory Early

```python
# ✅ Good
agent = ReactAgent(
    name="Agent",
    memory=ChromaMemory(collection_name="prod")
)

# ❌ Bad - harder to add later
agent = ReactAgent(name="Agent")
# ... agent.memory = ... (after initialization)
```

### 2. Use Descriptive Collection Names

```python
# ✅ Good
ChromaMemory(collection_name="customer_support_agent")

# ❌ Bad
ChromaMemory(collection_name="memory")
```

### 3. Clean Old Data

```python
# Periodically clear or archive old memories
if agent.memory.get_stats()['total_messages'] > 10000:
    # Archive or clear oldest messages
    agent.memory.clear()
```

### 4. Monitor Memory Usage

```python
stats = agent.memory.get_stats()
print(f"Memory: {stats['total_messages']} messages")

if stats['total_messages'] > 1000:
    print("⚠️  Consider using FAISS for better performance")
```

---

## Next Steps

<div class="grid cards" markdown>

-   :material-target: __Add Objectives__

    ---

    Give your agent goals to pursue

    [:octicons-arrow-right-24: Objectives System](objectives.md)

-   :material-creation: __Custom Memory Backends__

    ---

    Create your own memory implementation

    [:octicons-arrow-right-24: Memory Backends Guide](../guides/memory-backends.md)

-   :material-api: __API Reference__

    ---

    Complete memory API documentation

    [:octicons-arrow-right-24: Memory API](../api-reference/memory.md)

</div>

---

## Examples

Complete runnable examples:

- [memory_demo.py](https://github.com/marcosf63/react-agent-framework/blob/main/react_agent_framework/examples/memory_demo.py) - All memory backends demonstrated
- [Advanced Examples](../examples/advanced.md) - Complex memory usage patterns
