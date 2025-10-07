# ReAct Agent Framework - Informações do Projeto

## 📋 Informações Gerais

- **Nome do Projeto**: ReAct Agent Framework
- **Versão Atual**: 0.1.0
- **Tipo**: Framework Python para Agentes AI
- **Linguagem**: Python 3.8+
- **Licença**: MIT
- **Repositório**: https://github.com/marcosf63/react-agent-framework

## 🏗️ Arquitetura

### Estrutura de Diretórios
```
react-agent-framework/
├── react_agent_framework/      # Pacote principal
│   ├── core/                   # Núcleo do framework
│   │   ├── agent.py           # Implementação do agente ReAct
│   │   └── base.py            # Classes base
│   ├── tools/                  # Ferramentas built-in
│   │   ├── search.py          # Pesquisa web
│   │   └── calculator.py      # Calculadora
│   ├── cli/                    # Interface CLI
│   │   └── app.py             # Aplicação Typer
│   └── examples/               # Exemplos
│       ├── basic_usage.py
│       └── custom_tool.py
├── pyproject.toml              # Configuração do projeto
├── setup.py                    # Setup do pacote
├── CHANGELOG.md               # Histórico de versões
├── README.md                  # Documentação
└── LICENSE                    # Licença MIT
```

## 🔄 Versionamento (Semantic Versioning)

### Versão Atual: **0.1.0**

- **MAJOR (0)**: Versão inicial em desenvolvimento
- **MINOR (1)**: Primeira versão funcional
- **PATCH (0)**: Release inicial

### Como Versionar

Ao fazer mudanças, siga estas regras:

1. **PATCH** (0.1.X): Bug fixes e pequenas correções
   ```bash
   # Exemplo: 0.1.0 -> 0.1.1
   ```

2. **MINOR** (0.X.0): Novas funcionalidades (backward compatible)
   ```bash
   # Exemplo: 0.1.0 -> 0.2.0
   ```

3. **MAJOR** (X.0.0): Mudanças incompatíveis (breaking changes)
   ```bash
   # Exemplo: 0.1.0 -> 1.0.0
   ```

### Processo de Release

1. Atualizar versão em `pyproject.toml` e `react_agent_framework/__init__.py`
2. Atualizar `CHANGELOG.md` com as mudanças
3. Commitar mudanças
4. Criar tag git:
   ```bash
   git tag -a vX.Y.Z -m "Release vX.Y.Z - Descrição"
   ```
5. Push com tags:
   ```bash
   git push origin main --tags
   ```

## 🛠️ Desenvolvimento

### Ferramentas de Qualidade

- **Black**: Formatação de código (line-length: 100)
- **Ruff**: Linting moderno e rápido
- **Mypy**: Type checking estático

### Comandos Úteis

```bash
# Formatar código
black react_agent_framework/

# Verificar linting
ruff check react_agent_framework/

# Corrigir automaticamente
ruff check --fix react_agent_framework/

# Type checking
mypy react_agent_framework/ --ignore-missing-imports
```

## 📦 Instalação e Uso

### Desenvolvimento
```bash
pip install -e .
```

### CLI
```bash
react-agent perguntar "Sua pergunta"
react-agent interativo
```

### API Python
```python
from react_agent_framework import AgenteReAct
from react_agent_framework.tools import FerramentaPesquisa

ferramentas = [FerramentaPesquisa()]
agente = AgenteReAct(ferramentas=ferramentas)
resposta = agente.executar("Sua pergunta")
```

## 🚀 Roadmap

### v0.2.0 (Próxima versão)
- [ ] Suporte a outros LLMs (Anthropic Claude, Google Gemini)
- [ ] Sistema de memória para o agente
- [ ] Mais ferramentas built-in
- [ ] Testes unitários com pytest

### v1.0.0 (Versão estável)
- [ ] API estável e documentada
- [ ] Cobertura de testes >= 80%
- [ ] CI/CD completo
- [ ] Publicação no PyPI

## 📝 Notas de Desenvolvimento

### Padrões de Código

1. **Mensagens de Commit**: Seguir Conventional Commits
   - `feat:` Nova funcionalidade
   - `fix:` Correção de bug
   - `docs:` Mudanças na documentação
   - `refactor:` Refatoração de código
   - `test:` Adição/modificação de testes
   - `chore:` Tarefas de manutenção

2. **Type Hints**: Sempre usar type hints
3. **Docstrings**: Documentar todas as classes e funções públicas
4. **Testes**: Adicionar testes para novas funcionalidades

### Ambiente Virtual

```bash
# Criar
python -m venv .venv

# Ativar
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Instalar dependências
pip install -e ".[dev]"
```

## 🔗 Links Úteis

- **Repositório**: https://github.com/marcosf63/react-agent-framework
- **Issues**: https://github.com/marcosf63/react-agent-framework/issues
- **Documentação**: Ver README.md

---

Última atualização: 2025-10-06
Versão: 0.1.0
