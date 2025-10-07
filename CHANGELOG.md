# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

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
