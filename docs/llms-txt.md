# LLMs.txt - Complete Documentation for AI Models

The **LLMs.txt** file contains the complete framework documentation optimized for Large Language Model consumption.

---

## Overview

LLMs.txt is a comprehensive, structured documentation file designed specifically for AI models to understand and use the ReAct Agent Framework effectively.

**File Location**: [`LLMs.txt`](https://github.com/marcosf63/react-agent-framework/blob/main/LLMs.txt)

**Size**: 800+ lines
**Format**: Plain text with clear structure
**Coverage**: All versions from v0.1.0 to v0.12.0

---

## What's Included

### 1. Overview & Quick Start
Complete introduction with working examples

### 2. Installation
All installation methods and options

### 3. Core Concepts
ReAct pattern, agent creation, tool registration

### 4. Memory Systems (v0.10.0+)
- ChatMemory (SimpleChatMemory, SQLiteChatMemory)
- KnowledgeMemory (ChromaKnowledgeMemory, FAISSKnowledgeMemory)
- Complete API and examples

### 5. Multi-Provider Support
OpenAI, Anthropic, Google, Ollama configuration

### 6. Built-in Tools
Search, filesystem, computation tools

### 7. Objectives System
Goal tracking and management

### 8. Reasoning Strategies
ReAct, ReWOO, Reflection, Plan-Execute

### 9. Environments
Web, CLI, File environment interaction

### 10. MCP Integration
Model Context Protocol server setup

### 11. Layer 4: Infrastructure (v0.11.0)
Complete production infrastructure:
- **Monitoring**: Metrics, logging, telemetry
- **Resilience**: Retry, circuit breaker, fallback, timeout
- **Security**: RBAC, sandbox, audit, secrets
- **Cost Control**: Budget, rate limiting, quotas
- **Human-in-the-Loop**: Approval, intervention, feedback

### 12. Layer 3: Multi-Agent Systems (v0.12.0)
Complete multi-agent capabilities:
- **Communication**: Messages, protocols, channels
- **Orchestration**: Orchestrator, workflows, task delegation
- **Coordination**: Shared state, consensus, locking
- **Collaboration**: Teams, patterns, negotiation

### 13. Complete API Reference
All classes, methods, parameters, and return types

### 14. Examples & Use Cases
5 complete, production-ready examples:
1. Simple Q&A Agent
2. Research Agent with Memory
3. Production Agent with Infrastructure
4. Multi-Agent System
5. Complete Enterprise System

---

## Why LLMs.txt?

### For AI Models
- **Structured format** optimized for AI consumption
- **Complete coverage** of all features in one file
- **Working examples** with full context
- **No navigation required** - everything in sequence
- **Version tracking** - clear indication of feature versions

### For Developers
- **Quick reference** for AI pair programming
- **Copy-paste ready** code examples
- **Architecture overview** in one place
- **Version history** and migration paths

---

## How to Use

### As a Developer

**1. Share with AI assistants:**
```bash
# Copy to clipboard
cat LLMs.txt | pbcopy  # macOS
cat LLMs.txt | xclip   # Linux
```

**2. Reference in prompts:**
```
"Using the ReAct Agent Framework as described in LLMs.txt,
create an agent that..."
```

**3. Quick lookup:**
```bash
# Find specific topics
grep -A 10 "Multi-Agent" LLMs.txt
grep -A 20 "Memory Systems" LLMs.txt
```

### As an AI Model

The file is structured with clear section markers:
```
================================================================================
SECTION NAME
================================================================================
```

Each section includes:
- Concept explanation
- Code examples
- API signatures
- Best practices
- Common patterns

---

## Example Content Structure

```text
================================================================================
4. MEMORY SYSTEMS (v0.10.0+)
================================================================================

IMPORTANT: v0.10.0 separated memory into TWO types:
- Chat Memory: Sequential conversation history
- Knowledge Memory: Semantic knowledge base (RAG)

CHAT MEMORY:
------------

SimpleChatMemory (Development):
```python
from react_agent_framework.core.memory.chat import SimpleChatMemory

agent = ReactAgent(
    name="Agent",
    chat_memory=SimpleChatMemory(max_messages=100)
)
```

[... complete examples and API ...]
```

---

## Keeping Updated

The LLMs.txt file is updated with each release:

- **v0.12.0**: Added Layer 3 (Multi-Agent Systems)
- **v0.11.0**: Added Layer 4 (Infrastructure)
- **v0.10.0**: Added Memory System Refactoring
- **v0.9.0**: Initial LLMs.txt creation

---

## Download

**Direct link**: [LLMs.txt on GitHub](https://github.com/marcosf63/react-agent-framework/blob/main/LLMs.txt)

**Raw file**: [Raw LLMs.txt](https://raw.githubusercontent.com/marcosf63/react-agent-framework/main/LLMs.txt)

```bash
# Download with curl
curl -O https://raw.githubusercontent.com/marcosf63/react-agent-framework/main/LLMs.txt

# Download with wget
wget https://raw.githubusercontent.com/marcosf63/react-agent-framework/main/LLMs.txt
```

---

## Contribute

Found an issue or want to improve LLMs.txt?

1. [Open an issue](https://github.com/marcosf63/react-agent-framework/issues)
2. [Submit a PR](https://github.com/marcosf63/react-agent-framework/pulls)

The file is located at the repository root: `/LLMs.txt`

---

## See Also

- [Documentation Home](../index.md)
- [API Reference](../api-reference/react-agent.md)
- [Examples](../examples/basic-usage.md)
- [GitHub Repository](https://github.com/marcosf63/react-agent-framework)
