# Memory API Reference

Complete API reference for memory systems (v0.10.0+).

---

## Overview

Since v0.10.0, memory is split into two types:

- **Chat Memory**: Sequential conversation history
- **Knowledge Memory**: Semantic knowledge base (RAG)

---

## Chat Memory

### BaseChatMemory (Abstract)

Base interface for all chat memory implementations.

```python
from react_agent_framework.core.memory.chat import BaseChatMemory
```

#### Methods

**add_message(content: str, role: str = "user", metadata: Optional[Dict] = None) -> None**

Add a message to chat history.

**get_history(max_messages: Optional[int] = None) -> List[ChatMessage]**

Retrieve conversation history.

**clear() -> None**

Clear all chat history.

**get_stats() -> Dict[str, Any]**

Get memory statistics.

---

### SimpleChatMemory

In-memory chat buffer for development.

```python
from react_agent_framework.core.memory.chat import SimpleChatMemory

memory = SimpleChatMemory(max_messages=100)
```

---

### SQLiteChatMemory

Persistent chat storage with SQLite.

```python
from react_agent_framework.core.memory.chat import SQLiteChatMemory

memory = SQLiteChatMemory(
    db_path="./chat.db",
    session_id="user_123",
    max_messages=1000
)
```

---

## Knowledge Memory

### BaseKnowledgeMemory (Abstract)

Base interface for all knowledge memory implementations.

```python
from react_agent_framework.core.memory.knowledge import BaseKnowledgeMemory
```

#### Methods

**add_document(content: str, metadata: Optional[Dict] = None) -> str**

Add a document to knowledge base.

**search(query: str, top_k: int = 5, filter: Optional[Dict] = None) -> List[KnowledgeDocument]**

Semantic search for documents.

---

### ChromaKnowledgeMemory

Vector database using ChromaDB.

```python
from react_agent_framework.core.memory.knowledge import ChromaKnowledgeMemory

memory = ChromaKnowledgeMemory(
    collection_name="docs",
    persist_directory="./kb",
    embedding_function="default"
)
```

---

### FAISSKnowledgeMemory

High-performance vector search using FAISS.

```python
from react_agent_framework.core.memory.knowledge import FAISSKnowledgeMemory

memory = FAISSKnowledgeMemory(
    index_path="./faiss",
    dimension=384,
    index_type="Flat"
)
```

---

## See Also

- [Memory Systems Feature Guide](../features/memory-systems.md)
- [Memory Examples](../examples/memory-systems.md)
