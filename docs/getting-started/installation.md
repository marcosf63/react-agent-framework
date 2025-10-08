# Installation

Learn how to install ReAct Agent Framework in your project.

---

## Requirements

- **Python 3.8+**
- pip or uv package manager

---

## Install from PyPI

=== "Basic Installation"
    ```bash
    pip install react-agent-framework
    ```

=== "With MCP Support"
    ```bash
    pip install react-agent-framework[mcp]
    ```

=== "With All Providers"
    ```bash
    pip install react-agent-framework[anthropic,google]
    ```

=== "With Memory Backends"
    ```bash
    pip install react-agent-framework[chroma,faiss]
    ```

=== "Everything"
    ```bash
    pip install react-agent-framework[all]
    ```

---

## Install from Source

For development or to get the latest changes:

```bash
# Clone the repository
git clone https://github.com/marcosf63/react-agent-framework.git
cd react-agent-framework

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in editable mode
pip install -e .

# Or with all extras
pip install -e ".[all]"
```

---

## Optional Dependencies

### AI Providers

```bash
# Anthropic Claude
pip install react-agent-framework[anthropic]

# Google Gemini
pip install react-agent-framework[google]

# All providers
pip install react-agent-framework[anthropic,google]
```

### Memory Backends

```bash
# ChromaDB
pip install react-agent-framework[chroma]

# FAISS
pip install react-agent-framework[faiss]

# Both
pip install react-agent-framework[chroma,faiss]
```

### MCP Support

```bash
# Model Context Protocol
pip install react-agent-framework[mcp]
```

### Development Tools

```bash
# Development dependencies
pip install react-agent-framework[dev]
```

---

## Verify Installation

```python
from react_agent_framework import ReactAgent

# Check version
import react_agent_framework
print(react_agent_framework.__version__)  # Should print: 0.9.0

# Create a basic agent to test
agent = ReactAgent(name="Test Agent")
print(agent)  # Should print agent info
```

---

## Configuration

### API Keys

Create a `.env` file in your project root:

```env
# OpenAI (default provider)
OPENAI_API_KEY=sk-...

# Anthropic (optional)
ANTHROPIC_API_KEY=sk-ant-...

# Google (optional)
GOOGLE_API_KEY=AI...

# Other services (optional)
GITHUB_TOKEN=ghp_...
BRAVE_API_KEY=...
```

### Environment Variables

The framework automatically loads environment variables from `.env` files using `python-dotenv`.

---

## Next Steps

- :material-rocket: [Quickstart Guide](quickstart.md) - Get started in 5 minutes
- :material-robot: [Your First Agent](first-agent.md) - Build your first agent
- :material-book: [Features Overview](../features/multi-provider.md) - Explore all features

---

## Troubleshooting

### ImportError: No module named 'react_agent_framework'

Make sure you've installed the package:

```bash
pip install react-agent-framework
```

### Provider not found

Install the specific provider:

```bash
pip install react-agent-framework[anthropic]  # For Claude
pip install react-agent-framework[google]     # For Gemini
```

### MCP tools not working

Install MCP support:

```bash
pip install react-agent-framework[mcp]
```

---

!!! tip "Using Virtual Environments"
    Always use virtual environments to isolate dependencies:

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```
