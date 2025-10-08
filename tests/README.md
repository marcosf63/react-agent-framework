# Testes do ReAct Agent Framework

Este diretório contém os testes unitários do ReAct Agent Framework usando pytest.

## Estrutura dos Testes

- **test_imports.py**: Testa imports e exports do pacote
- **test_providers.py**: Testa providers LLM (OpenAI, Anthropic, Google, Ollama)
- **test_memory.py**: Testa sistema de memória (SimpleMemory, ChromaMemory, FAISSMemory)
- **conftest.py**: Fixtures compartilhadas para todos os testes

## Executando os Testes

### Todos os testes
```bash
pytest
```

### Com cobertura de código
```bash
pytest --cov=react_agent_framework --cov-report=html
```

### Testes específicos
```bash
pytest tests/test_providers.py -v
pytest tests/test_memory.py::TestSimpleMemory -v
```

### Com output detalhado
```bash
pytest -vv
```

## Cobertura Atual

- **77 testes** todos passando
- **25%** de cobertura de código

### Áreas Cobertas
- ✅ Imports e exports
- ✅ Provider factory
- ✅ OpenAI provider (100%)
- ✅ Ollama provider (87%)
- ✅ SimpleMemory (87%)
- ✅ Message classes

### Áreas para Expansão
- ⏳ ReactAgent core
- ⏳ Tools system
- ⏳ Environments (Web, CLI, File)
- ⏳ Objectives tracker
- ⏳ Reasoning strategies

## Fixtures Disponíveis

### Providers
- `mock_openai_provider`: Mock do OpenAI provider
- `mock_anthropic_provider`: Mock do Anthropic provider
- `mock_ollama_provider`: Mock do Ollama provider

### Agents
- `simple_agent`: Agent básico para testes
- `agent_with_tool`: Agent com tool registrada

### Data
- `sample_messages`: Mensagens de exemplo
- `sample_objectives`: Objectives de exemplo

## Configuração

- **pytest.ini**: Configuração do pytest
- **.coveragerc**: Configuração de cobertura
- **pyproject.toml**: Configuração do projeto (inclui dependências de dev)

## Dependências de Desenvolvimento

```bash
pip install -e ".[dev]"
```

Inclui:
- pytest
- pytest-cov
- coverage
