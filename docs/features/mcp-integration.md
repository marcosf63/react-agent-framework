# MCP Integration

Connect your agents to Model Context Protocol (MCP) servers to access external tools dynamically.

---

## What is MCP?

[Model Context Protocol (MCP)](https://modelcontextprotocol.io) is Anthropic's open standard for connecting AI assistants to data sources and tools.

### Benefits

- :material-connection: Connect to external tool servers
- :material-auto-fix: Auto-discover available tools
- :material-security: Secure tool execution
- :material-language-python: Works with any MCP-compatible server

---

## Installation

```bash
pip install react-agent-framework[mcp]
```

---

## Basic Usage

```python
from react_agent_framework import ReactAgent

# Create agent
agent = ReactAgent(name="MCP Agent")

# Connect to filesystem MCP server
server_id = agent.add_mcp_server(
    command="npx",
    args=["-y", "@modelcontextprotocol/server-filesystem", "/tmp"],
    name="filesystem"
)

# All tools from the server are now available!
answer = agent.run("List files in the /tmp directory")
```

---

## Popular MCP Servers

### Filesystem Server

Access local files and directories:

```python
agent.add_mcp_server(
    command="npx",
    args=["-y", "@modelcontextprotocol/server-filesystem", "/path/to/dir"],
    name="filesystem"
)
```

### GitHub Server

Interact with GitHub repositories:

```python
agent.add_mcp_server(
    command="npx",
    args=["-y", "@modelcontextprotocol/server-github"],
    env={"GITHUB_TOKEN": "ghp_your_token"},
    name="github"
)
```

### PostgreSQL Server

Query databases:

```python
agent.add_mcp_server(
    command="npx",
    args=["-y", "@modelcontextprotocol/server-postgres"],
    env={"POSTGRES_CONNECTION_STRING": "postgresql://..."},
    name="postgres"
)
```

### Puppeteer Server

Browser automation:

```python
agent.add_mcp_server(
    command="npx",
    args=["-y", "@modelcontextprotocol/server-puppeteer"],
    name="puppeteer"
)
```

---

## Managing Servers

### List Connected Servers

```python
servers = agent.list_mcp_servers()
for server in servers:
    print(f"{server['name']}: {server['num_tools']} tools")
```

### List Available Tools

```python
tools = agent.list_mcp_tools()
for tool_desc in tools:
    print(tool_desc)
```

### Disconnect from Server

```python
agent.disconnect_mcp_server(server_id)
```

---

## Using Config Files

Create `mcp_config.json`:

```json
{
  "servers": [
    {
      "name": "filesystem",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/tmp"],
      "auto_connect": true
    },
    {
      "name": "github",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_..."
      },
      "auto_connect": false
    }
  ]
}
```

Load config:

```python
from react_agent_framework.mcp.config import MCPConfigManager

config_manager = MCPConfigManager("mcp_config.json")

for server_name in config_manager.list_servers():
    server_config = config_manager.get_server(server_name)
    agent.add_mcp_server(
        command=server_config.command,
        args=server_config.args,
        env=server_config.env,
        name=server_config.name
    )
```

---

## Complete Example

```python
from react_agent_framework import ReactAgent

# Create agent
agent = ReactAgent(
    name="Multi-Source Agent",
    description="Agent with access to multiple data sources",
    provider="gpt-4o-mini"
)

# Connect to filesystem
fs_server = agent.add_mcp_server(
    command="npx",
    args=["-y", "@modelcontextprotocol/server-filesystem", "."],
    name="filesystem"
)

# Connect to GitHub (if token available)
try:
    gh_server = agent.add_mcp_server(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-github"],
        env={"GITHUB_TOKEN": "ghp_..."},
        name="github"
    )
except:
    print("GitHub server not configured")

# List all available tools
print("\nAvailable MCP Tools:")
for tool in agent.list_mcp_tools():
    print(f"  - {tool}")

# Use the agent
tasks = [
    "List all Python files in current directory",
    "Read the contents of README.md",
]

for task in tasks:
    print(f"\nTask: {task}")
    result = agent.run(task)
    print(f"Result: {result}")

# Cleanup
agent.disconnect_mcp_server(fs_server)
```

---

## Creating Custom MCP Servers

You can create your own MCP servers. See the [MCP Python SDK documentation](https://github.com/anthropics/python-sdk-mcp) for details.

Example custom server:

```python
from mcp import Server, Tool

server = Server("my-custom-server")

@server.tool()
async def my_custom_tool(param: str) -> str:
    """My custom tool"""
    return f"Processed: {param}"

if __name__ == "__main__":
    server.run()
```

Use it:

```python
agent.add_mcp_server(
    command="python",
    args=["my_custom_server.py"],
    name="custom"
)
```

---

## API Reference

For detailed API documentation, see:

- [MCP Client Reference](../api-reference/mcp.md)
- [ReactAgent MCP Methods](../api-reference/react-agent.md#mcp-methods)

---

## Learn More

- [Official MCP Documentation](https://modelcontextprotocol.io)
- [MCP Python SDK](https://github.com/anthropics/python-sdk-mcp)
- [Available MCP Servers](https://github.com/modelcontextprotocol/servers)
