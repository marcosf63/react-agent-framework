# Memory Systems

Give your agents the ability to remember conversations and retrieve relevant knowledge.

---

## Overview

Since **v0.10.0**, the memory system has been refactored into **two specialized types**:

**Chat Memory**: Sequential conversation history for maintaining dialogue context
**Knowledge Memory**: Semantic knowledge retrieval (RAG) for storing and searching facts using vector similarity

---

## Quick Start

```python
from react_agent_framework import ReactAgent
from react_agent_framework.core.memory.chat import SQLiteChatMemory
from react_agent_framework.core.memory.knowledge import ChromaKnowledgeMemory

agent = ReactAgent(
    name="Smart Assistant",
    chat_memory=SQLiteChatMemory("./chat.db"),
    knowledge_memory=ChromaKnowledgeMemory("./knowledge")
)
```

See [complete documentation](https://marcosf63.github.io/react-agent-framework/features/memory-systems/) for details.
