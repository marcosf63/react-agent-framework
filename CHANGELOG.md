# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [0.9.0] - 2025-10-07

### Adicionado
- **Multi-Provider Support**: Suporte completo para OpenAI, Anthropic Claude, Google Gemini e Ollama
- **MCP Integration**: Integração com Model Context Protocol para conectar a servidores externos
- **Environment System**: Três ambientes integrados (Web, CLI, File) para interação estruturada
- **Memory Systems**: Três backends de memória (SimpleMemory, ChromaMemory, FAISSMemory)
- **Objectives System**: Sistema de objetivos com prioridades e tracking de progresso
- **Built-in Tools**: Ferramentas integradas de busca, sistema de arquivos e computação
- **Reasoning Strategies**: Implementação completa do padrão ReAct com controle de iterações
- **Complete Documentation**: Documentação profissional com Material for MkDocs (https://marcosf63.github.io/react-agent-framework/)

### Melhorado
- API estilo FastAPI com decoradores `@agent.tool()`
- Suporte completo a type hints
- Auto-detecção de providers baseado em model name
- Sistema de configuração via URL-style strings
- Tratamento robusto de erros
- Modo verbose para debugging
- CLI interativa melhorada

### Documentação
- 30+ páginas de documentação completa
- 10+ exemplos práticos de uso
- Guias de customização (providers, tools, memory)
- Documentação de API Reference
- Best practices e troubleshooting
- Auto-deploy via GitHub Actions

### Extras Opcionais
- `pip install react-agent-framework[anthropic]` - Suporte Anthropic Claude
- `pip install react-agent-framework[google]` - Suporte Google Gemini
- `pip install react-agent-framework[mcp]` - Model Context Protocol
- `pip install react-agent-framework[memory-chroma]` - ChromaDB memory
- `pip install react-agent-framework[memory-faiss]` - FAISS memory
- `pip install react-agent-framework[all]` - Todos os extras

[0.9.0]: https://github.com/marcosf63/react-agent-framework/releases/tag/v0.9.0

## [0.1.0] - 2025-10-06

### Adicionado
- Implementação inicial do ReAct Agent Framework
- Core do framework com classe `AgenteReAct`
- Sistema de ferramentas extensível via classe base `Ferramenta`
- Ferramentas built-in:
  - `FerramentaPesquisa`: Pesquisa na internet via DuckDuckGo
  - `FerramentaCalculadora`: Calculadora matemática
- CLI interativa usando Typer
  - Comando `perguntar` para fazer perguntas únicas
  - Comando `interativo` para sessões de perguntas múltiplas
  - Comando `versao` para ver versão do framework
  - Suporte a modo verbose (`--verbose` / `-v`)
  - Seleção de modelo OpenAI (`--modelo` / `-m`)
- Interface Rich para output colorido e formatado
- Exemplos de uso:
  - `basic_usage.py`: Exemplo básico
  - `custom_tool.py`: Como criar ferramentas personalizadas
- Documentação completa no README.md
- Configuração de qualidade de código:
  - Black para formatação
  - Ruff para linting
  - Mypy para type checking
- Suporte a instalação via pip (`pip install -e .`)
- Licença MIT
- Type hints completos
- Estrutura modular profissional

### Configuração
- Python 3.8+ suportado
- Semantic Versioning implementado
- GitHub Actions pronto para CI/CD (futuro)

[0.1.0]: https://github.com/marcosf63/react-agent-framework/releases/tag/v0.1.0
