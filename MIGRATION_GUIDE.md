# Memory System Refactoring - Migration Guide

## 🎯 Overview

Version 0.10.0 introduces a major refactoring of the memory system, separating it into two distinct types:

1. **Chat Memory** - Conversation history (sequential storage)
2. **Knowledge Memory** - RAG/Semantic search (vector-based)

## 🔄 What Changed?

### Old Structure (v0.9.x)
```
memory/
├── base.py          # BaseMemory
├── simple.py        # SimpleMemory
├── chroma.py        # ChromaMemory (mixed purpose)
└── faiss.py         # FAISSMemory (mixed purpose)
```

### New Structure (v0.10.0)
```
memory/
├── chat/            # Conversation history
│   ├── base.py      # BaseChatMemory
│   ├── simple.py    # SimpleChatMemory
│   └── sqlite.py    # SQLiteChatMemory (NEW!)
│
├── knowledge/       # RAG / Semantic search
│   ├── base.py      # BaseKnowledgeMemory
│   ├── chroma.py    # ChromaKnowledgeMemory
│   └── faiss.py     # FAISSKnowledgeMemory
│
└── adapters.py      # Backward compatibility
```

## 📦 Package Names

### Old Package Names (deprecated but still work)
```python
from react_agent_framework.core.memory import SimpleMemory
from react_agent_framework.core.memory import ChromaMemory
from react_agent_framework.core.memory import FAISSMemory
```

### New Package Names (recommended)
```python
# Chat memory
from react_agent_framework.core.memory.chat import SimpleChatMemory
from react_agent_framework.core.memory.chat import SQLiteChatMemory

# Knowledge memory
from react_agent_framework.core.memory.knowledge import ChromaKnowledgeMemory
from react_agent_framework.core.memory.knowledge import FAISSKnowledgeMemory
```

## 🔧 Installation

### Chat Memory (SQLite)
```bash
pip install react-agent-framework  # SQLite included (stdlib)
```

### Knowledge Memory
```bash
# ChromaDB
pip install react-agent-framework[knowledge-chroma]

# FAISS
pip install react-agent-framework[knowledge-faiss]

# Both
pip install react-agent-framework[all-memory]
```

## 💡 Migration Examples

### Example 1: Simple Memory (Chat History)

**Old Code (v0.9.x):**
```python
from react_agent_framework import ReactAgent
from react_agent_framework.core.memory import SimpleMemory

agent = ReactAgent(
    name="Assistant",
    memory=SimpleMemory(max_messages=100)
)
```

**New Code (v0.10.0):**
```python
from react_agent_framework import ReactAgent
from react_agent_framework.core.memory.chat import SimpleChatMemory

agent = ReactAgent(
    name="Assistant",
    chat_memory=SimpleChatMemory(max_messages=100)
)
```

### Example 2: Persistent Chat History (NEW!)

```python
from react_agent_framework import ReactAgent
from react_agent_framework.core.memory.chat import SQLiteChatMemory

agent = ReactAgent(
    name="Assistant",
    chat_memory=SQLiteChatMemory(
        db_path="./conversations.db",
        session_id="user_123"
    )
)

# Chat history persists across restarts!
agent.run("Hello!")
# Later...
agent.run("What did we talk about?")  # Remembers previous conversation
```

### Example 3: RAG with Knowledge Memory

**Old Code (mixed purpose):**
```python
from react_agent_framework import ReactAgent
from react_agent_framework.core.memory import ChromaMemory

agent = ReactAgent(
    name="Assistant",
    memory=ChromaMemory(collection_name="docs")
)

# This was confusing - was it for chat or RAG?
agent.memory.add("Python is a programming language", role="system")
```

**New Code (clear separation):**
```python
from react_agent_framework import ReactAgent
from react_agent_framework.core.memory.chat import SQLiteChatMemory
from react_agent_framework.core.memory.knowledge import ChromaKnowledgeMemory

agent = ReactAgent(
    name="Assistant",
    chat_memory=SQLiteChatMemory("./chat.db"),           # Conversation history
    knowledge_memory=ChromaKnowledgeMemory("./kb")       # RAG knowledge base
)

# Add documents to knowledge base
agent.knowledge_memory.add_document(
    "Python is a programming language",
    metadata={"category": "programming"}
)

# Search knowledge base
results = agent.knowledge_memory.search("programming languages", top_k=3)
for doc in results:
    print(doc.content)
```

### Example 4: Combined Chat + Knowledge

```python
from react_agent_framework import ReactAgent
from react_agent_framework.core.memory.chat import SQLiteChatMemory
from react_agent_framework.core.memory.knowledge import FAISSKnowledgeMemory

# Create agent with both types
agent = ReactAgent(
    name="Technical Assistant",
    chat_memory=SQLiteChatMemory("./chat.db"),
    knowledge_memory=FAISSKnowledgeMemory("./tech_docs")
)

# Load technical documentation
docs = [
    "Docker is a containerization platform",
    "Kubernetes orchestrates containers",
    "FastAPI is a modern Python web framework"
]
agent.knowledge_memory.add_documents(docs)

# Chat with RAG
answer = agent.run("How do I deploy a FastAPI app with Docker?")
# Agent uses:
# 1. chat_memory for conversation context
# 2. knowledge_memory for technical documentation
```

## 🔑 Key Differences

### Chat Memory (Conversation History)
- **Purpose**: Store sequential chat history
- **Storage**: SQLite, in-memory
- **Retrieval**: Chronological order, simple keyword search
- **Use Case**: Maintain conversation context

### Knowledge Memory (RAG)
- **Purpose**: Store documents for semantic search
- **Storage**: Vector databases (ChromaDB, FAISS)
- **Retrieval**: Semantic similarity search
- **Use Case**: Retrieval Augmented Generation

## ⚙️ ReactAgent API Changes

### Old API (still works via adapters)
```python
agent = ReactAgent(
    memory=SimpleMemory()  # Deprecated
)
```

### New API (recommended)
```python
agent = ReactAgent(
    chat_memory=SimpleChatMemory(),        # Chat history
    knowledge_memory=ChromaKnowledgeMemory()  # RAG (optional)
)
```

## 🛠️ Backward Compatibility

**The old API still works!** We provide adapters for backward compatibility:

```python
from react_agent_framework import ReactAgent
from react_agent_framework.core.memory import SimpleMemory  # Old import

agent = ReactAgent(
    memory=SimpleMemory()  # Still works!
)
```

However, you should migrate to the new API for:
- ✅ Better performance
- ✅ Clear separation of concerns
- ✅ Access to new features (SQLite, better RAG)
- ✅ Future-proof code

## 📊 Comparison Table

| Feature | Old (v0.9.x) | New Chat (v0.10.0) | New Knowledge (v0.10.0) |
|---------|--------------|-------------------|------------------------|
| **Purpose** | Mixed | Conversation history | RAG/Search |
| **Storage** | In-memory/Vector | In-memory/SQLite | Vector DB |
| **Persistence** | Limited | ✅ SQLite | ✅ ChromaDB/FAISS |
| **Search** | Basic | Keyword | Semantic |
| **Sessions** | Basic | ✅ Multi-session | N/A |
| **Scalability** | Low | Medium | High |

## 🚀 Next Steps

1. **Update imports** - Use new `chat` and `knowledge` packages
2. **Separate concerns** - Use chat memory for history, knowledge memory for RAG
3. **Try SQLite** - Persistent chat history without external dependencies
4. **Leverage RAG** - Use knowledge memory for document search

## 📚 Resources

- [Chat Memory Documentation](docs/features/chat-memory.md)
- [Knowledge Memory Documentation](docs/features/knowledge-memory.md)
- [Complete API Reference](docs/api-reference/memory.md)
- [Examples](react_agent_framework/examples/memory_demo.py)
