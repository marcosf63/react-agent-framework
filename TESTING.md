# Guia de Testes e CI/CD

## Testes Locais

### Executar todos os testes
```bash
pytest
```

### Com cobertura
```bash
pytest --cov=react_agent_framework --cov-report=html
```

### Testes específicos
```bash
pytest tests/test_providers.py -v
pytest tests/test_memory.py::TestSimpleMemory::test_add_message -v
```

## CI/CD GitHub Actions

### Workflows Configurados

#### 1. **Test Workflow** (`.github/workflows/test.yml`)
- **Trigger**: Push ou Pull Request
- **Ação**: Roda todos os testes com pytest
- **Matriz**: Python 3.8, 3.9, 3.10, 3.11, 3.12
- **OS**: Ubuntu, Windows, macOS

#### 2. **Publish PyPI Workflow** (`.github/workflows/publish-pypi.yml`)
- **Trigger**: Push de tag `v*.*.*`
- **Ação**: Publica automaticamente no PyPI
- **Requer**: Testes passando primeiro

### Configurar Secrets no GitHub

Para que os workflows funcionem, configure os seguintes secrets:

1. Acesse: `https://github.com/marcosf63/react-agent-framework/settings/secrets/actions`

2. Adicione os secrets:

   - **PYPI_API_TOKEN**
     - Valor: `pypi-...` (seu token do PyPI)
     - Usado para publicação no PyPI production

   - **TEST_PYPI_API_TOKEN**
     - Valor: `pypi-...` (seu token do TestPyPI)
     - Usado para publicação no TestPyPI (opcional, para testes)

### Como Obter os Tokens

#### PyPI Token
1. Acesse: https://pypi.org/manage/account/token/
2. Clique em "Add API token"
3. Nome: `GitHub Actions - react-agent-framework`
4. Scope: `Project: react-agent-framework`
5. Copie o token (começa com `pypi-`)

#### TestPyPI Token
1. Acesse: https://test.pypi.org/manage/account/token/
2. Repita o mesmo processo

## Workflow de Desenvolvimento

### 1. Desenvolvimento Normal
```bash
# Fazer alterações
git add .
git commit -m "feat: nova funcionalidade"
git push
```
- ✅ Testes rodam automaticamente
- ✅ Verifica em múltiplas versões do Python
- ✅ Verifica em múltiplos sistemas operacionais

### 2. Publicar Nova Versão

```bash
# 1. Atualizar versão em pyproject.toml
vim pyproject.toml  # version = "0.10.0"

# 2. Atualizar CHANGELOG.md
vim CHANGELOG.md

# 3. Commit das alterações
git add pyproject.toml CHANGELOG.md
git commit -m "chore: bump version to 0.10.0"
git push

# 4. Criar tag
git tag v0.10.0
git push origin v0.10.0
```

- ✅ Workflow de testes roda primeiro
- ✅ Se testes passarem, publica no TestPyPI
- ✅ Se TestPyPI OK, publica no PyPI
- ✅ Cria GitHub Release automaticamente

## Status dos Testes

### Cobertura Atual: 25%

#### Módulos Testados (≥80%)
- ✅ `__init__.py` - 100%
- ✅ `providers/openai_provider.py` - 100%
- ✅ `providers/factory.py` - 97%
- ✅ `providers/ollama_provider.py` - 88%
- ✅ `memory/simple.py` - 87%
- ✅ `memory/base.py` - 85%
- ✅ `providers/base.py` - 85%

#### Para Expandir
- ⏳ `core/react_agent.py` - 17%
- ⏳ `tools/` - 30-40%
- ⏳ `core/environment/` - 0%
- ⏳ `core/reasoning/` - 0%
- ⏳ `mcp/` - 15-30%

## Estrutura dos Testes

```
tests/
├── README.md              # Documentação dos testes
├── __init__.py
├── conftest.py            # Fixtures compartilhadas
├── test_imports.py        # Testa imports (15 testes)
├── test_providers.py      # Testa providers (30 testes)
└── test_memory.py         # Testa memória (32 testes)
```

## Fixtures Disponíveis

```python
# Providers mockados
def test_something(mock_openai_provider):
    assert mock_openai_provider.generate(...) == "Mocked response"

# Agent simples
def test_agent(simple_agent):
    assert simple_agent.name == "Test Agent"

# Agent com tool
def test_tool(agent_with_tool):
    result = agent_with_tool.tools["test_tool"]()
    assert result == "test result"

# Dados de exemplo
def test_messages(sample_messages):
    assert len(sample_messages) == 3

def test_objectives(sample_objectives):
    assert len(sample_objectives) == 2
```

## Verificar Status do CI/CD

1. **Actions Tab**: https://github.com/marcosf63/react-agent-framework/actions
2. **Último workflow**: Mostra status dos testes
3. **Badge**: Adicione ao README.md:

```markdown
![Tests](https://github.com/marcosf63/react-agent-framework/actions/workflows/test.yml/badge.svg)
```

## Troubleshooting

### Testes falhando no CI mas passam localmente
- Verifique versão do Python
- Verifique dependências opcionais
- Rode: `pytest --tb=short` para ver erros

### Publicação no PyPI falha
- Verifique se PYPI_API_TOKEN está configurado
- Verifique se a versão já existe no PyPI
- Verifique logs do workflow

### Workflow não executou
- Verifique se o push foi para `main`
- Verifique se a tag segue o formato `v*.*.*`
- Verifique se há erros no YAML do workflow
