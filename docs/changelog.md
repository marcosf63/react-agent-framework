# Changelog

All notable changes to ReAct Agent Framework are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.9.0] - 2025-01-07

### Added
- **MCP Integration**: Full support for Model Context Protocol
  - `MCPClient` for managing server connections
  - `MCPToolAdapter` for tool integration
  - `MCPConfigManager` for server configuration
  - `add_mcp_server()` method in ReactAgent
  - Support for popular MCP servers (filesystem, github, postgres, etc.)
- MCP demo example in `examples/mcp_demo.py`
- Complete documentation site with Material for MkDocs

### Changed
- Updated package description to include MCP support
- Enhanced ReactAgent with MCP methods

---

## [0.8.0] - 2025-01-06

### Added
- **Environment System**: Agent-environment interaction framework
  - `BaseEnvironment` abstract class
  - `WebEnvironment` for browser automation
  - `CLIEnvironment` for shell command execution
  - `FileEnvironment` for file operations
  - `EnvironmentState` for state tracking
  - Safe mode for all environments

---

## [0.7.0] - 2025-01-06

### Added
- **Reasoning Strategies**: Multiple reasoning approaches
  - `ReActReasoning`: Iterative thought-action-observation
  - `ReWOOReasoning`: Plan-then-execute (Reasoning Without Observation)
  - `ReflectionReasoning`: Self-critique and improve
  - `PlanExecuteReasoning`: Adaptive planning with updates
  - `BaseReasoning` abstract class
  - `ReasoningResult` dataclass

---

## [0.6.0] - 2025-01-05

### Added
- **Objectives System**: Goal-oriented agent management
  - `Objective` class with priority levels
  - `ObjectiveTracker` for managing multiple objectives
  - Progress tracking and status management
  - Success criteria support
  - Integration with ReactAgent

---

## [0.5.0] - 2025-01-05

### Added
- **Memory Systems**: Context retention across conversations
  - `SimpleMemory`: In-memory conversation history
  - `ChromaMemory`: Vector-based memory with ChromaDB
  - `FAISSMemory`: High-performance similarity search
  - `BaseMemory` abstract class

---

## [0.4.0] - 2025-01-04

### Added
- **Built-in Tools System**: Registry-based tool management
  - `ToolRegistry` for discovering and managing tools
  - `use_tools()` method with pattern matching
  - Filesystem tools (read, write, list, delete)
  - Computation tools (calculator, code executor, shell)
  - Search tools (DuckDuckGo)

---

## [0.3.0] - 2025-01-04

### Added
- **Multi-Provider Support**: Support for multiple LLM providers
  - OpenAI (default)
  - Anthropic Claude
  - Google Gemini
  - Ollama (local)
  - `BaseLLMProvider` abstract class
  - Provider factory for easy switching

---

## [0.2.0] - 2025-01-03

### Added
- FastAPI-style API with decorators
- `@agent.tool()` decorator for registering tools
- Rich configuration options
- Type hints throughout

### Changed
- Improved API design
- Better error handling

---

## [0.1.0] - 2025-01-02

### Added
- Initial release
- Basic ReactAgent implementation
- ReAct pattern (Reasoning + Acting)
- OpenAI integration
- CLI with Typer and Rich
- Basic examples

---

## Future Releases

### Planned for 1.0.0
- Stable API
- Comprehensive test coverage (>80%)
- Full CI/CD pipeline
- PyPI publication
- Production-ready documentation

### Under Consideration
- More LLM providers
- Additional reasoning strategies
- Advanced tool system
- Plugin architecture
- Web UI for agent monitoring

---

For detailed changes, see [GitHub Releases](https://github.com/marcosf63/react-agent-framework/releases).
