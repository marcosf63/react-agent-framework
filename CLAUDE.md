# ReAct Agent Framework - Informações do Projeto

## 📋 Informações Gerais

- **Nome do Projeto**: ReAct Agent Framework
- **Versão Atual**: 0.11.0
- **Tipo**: Framework Python para Agentes AI Production-Ready
- **Linguagem**: Python 3.9+
- **Licença**: MIT
- **Repositório**: https://github.com/marcosf63/react-agent-framework
- **Documentação**: https://marcosf63.github.io/react-agent-framework/

## 🏗️ Arquitetura

### Estrutura de Diretórios
```
react-agent-framework/
├── react_agent_framework/          # Pacote principal
│   ├── core/                       # Núcleo do framework
│   │   ├── react_agent.py         # ReactAgent principal
│   │   ├── memory/                # Sistemas de memória
│   │   │   ├── simple.py          # Memória simples
│   │   │   ├── chroma.py          # ChromaDB backend
│   │   │   └── faiss.py           # FAISS backend
│   │   ├── objectives/            # Sistema de objetivos
│   │   │   ├── objective.py       # Classe Objective
│   │   │   └── tracker.py         # ObjectiveTracker
│   │   ├── reasoning/             # Estratégias de raciocínio
│   │   │   ├── react.py           # ReAct pattern
│   │   │   ├── rewoo.py           # ReWOO pattern
│   │   │   ├── reflection.py      # Reflection pattern
│   │   │   └── plan_execute.py    # Plan-Execute pattern
│   │   └── environment/           # Ambientes de interação
│   │       ├── web.py             # Ambiente web
│   │       ├── cli.py             # Ambiente CLI
│   │       └── file.py            # Ambiente de arquivos
│   ├── providers/                 # Provedores de LLM
│   │   ├── openai_provider.py    # OpenAI
│   │   ├── anthropic_provider.py # Anthropic
│   │   ├── google_provider.py    # Google
│   │   └── ollama_provider.py    # Ollama
│   ├── tools/                     # Ferramentas built-in
│   │   ├── search/                # Ferramentas de busca
│   │   ├── filesystem/            # Ferramentas de sistema de arquivos
│   │   └── computation/           # Ferramentas de computação
│   ├── mcp/                       # Model Context Protocol
│   │   ├── client.py              # Cliente MCP
│   │   ├── adapter.py             # Adaptador de tools
│   │   └── config.py              # Gerenciador de configuração
│   ├── infrastructure/            # Layer 4: Agentic Infrastructure
│   │   ├── monitoring/            # Monitoring System
│   │   │   ├── metrics.py         # AgentMetrics (Prometheus)
│   │   │   ├── logger.py          # AgentLogger (JSON logging)
│   │   │   └── telemetry.py       # AgentTelemetry (tracing)
│   │   ├── resilience/            # Resilience System
│   │   │   ├── retry.py           # RetryStrategy
│   │   │   ├── circuit_breaker.py # CircuitBreaker
│   │   │   ├── fallback.py        # FallbackStrategy
│   │   │   └── timeout.py         # TimeoutManager
│   │   ├── security/              # Security System
│   │   │   ├── permissions.py     # RBACManager
│   │   │   ├── sandbox.py         # Sandbox
│   │   │   ├── audit.py           # AuditLogger
│   │   │   └── secrets.py         # SecretsManager
│   │   ├── cost_control/          # Cost Control System
│   │   │   ├── budget.py          # BudgetTracker
│   │   │   ├── rate_limiter.py    # RateLimiter
│   │   │   └── quota.py           # QuotaManager
│   │   └── human_loop/            # Human-in-the-Loop System
│   │       ├── approval.py        # ApprovalManager
│   │       ├── intervention.py    # InterventionManager
│   │       └── feedback.py        # FeedbackCollector
│   ├── cli/                       # Interface CLI
│   │   └── app.py                 # Aplicação Typer
│   └── examples/                  # Exemplos
│       ├── fastapi_style.py
│       ├── custom_tools.py
│       ├── multi_provider.py
│       ├── memory_demo.py
│       ├── objectives_demo.py
│       ├── mcp_demo.py
│       ├── infrastructure_monitoring_demo.py
│       ├── infrastructure_resilience_demo.py
│       ├── infrastructure_security_demo.py
│       ├── infrastructure_cost_control_demo.py
│       └── infrastructure_human_loop_demo.py
├── docs/                          # Documentação (MkDocs)
│   ├── index.md                   # Página inicial
│   ├── getting-started/           # Guias de início
│   ├── features/                  # Documentação de features
│   ├── guides/                    # Guias práticos
│   ├── api-reference/             # Referência da API
│   └── examples/                  # Exemplos documentados
├── .github/workflows/             # GitHub Actions
│   └── docs.yml                   # Deploy da documentação
├── pyproject.toml                 # Configuração do projeto
├── mkdocs.yml                     # Configuração MkDocs
├── requirements-docs.txt          # Dependências da documentação
├── CHANGELOG.md                   # Histórico de versões
├── README.md                      # Documentação principal
└── LICENSE                        # Licença MIT
```

## 🔄 Versionamento (Semantic Versioning)

### Versão Atual: **0.11.0** 🚀

### Histórico de Versões

- **0.11.0** (2025-01-11): Layer 4 - Agentic Infrastructure (Production-Ready)
  - Part 1/5: Monitoring (Metrics, Logger, Telemetry)
  - Part 2/5: Resilience (Retry, Circuit Breaker, Fallback, Timeout)
  - Part 3/5: Security (RBAC, Sandbox, Audit, Secrets)
  - Part 4/5: Cost Control (Budget, Rate Limiter, Quota)
  - Part 5/5: Human-in-the-Loop (Approval, Intervention, Feedback)
- **0.10.1** (2025-01-11): Memory System Bugfixes (interface compatibility)
- **0.10.0** (2025-01-10): Memory System Refactoring (Chat + Knowledge separation)
- **0.9.1** (2025-01-08): Bugfixes e melhorias
- **0.9.0** (2025-01-07): MCP Integration + Documentação completa
- **0.8.0** (2025-01-06): Environment System
- **0.7.0** (2025-01-06): Reasoning Strategies
- **0.6.0** (2025-01-05): Objectives System
- **0.5.0** (2025-01-05): Memory Systems
- **0.4.0** (2025-01-04): Built-in Tools System
- **0.3.0** (2025-01-04): Multi-Provider Support
- **0.2.0** (2025-01-03): FastAPI-style API
- **0.1.0** (2025-01-02): Release inicial

### Como Versionar

Ao fazer mudanças, siga estas regras:

1. **PATCH** (0.9.X): Bug fixes e pequenas correções
   ```bash
   # Exemplo: 0.9.0 -> 0.9.1
   ```

2. **MINOR** (0.X.0): Novas funcionalidades (backward compatible)
   ```bash
   # Exemplo: 0.9.0 -> 0.10.0
   ```

3. **MAJOR** (X.0.0): Mudanças incompatíveis (breaking changes)
   ```bash
   # Exemplo: 0.9.0 -> 1.0.0
   ```

### Processo de Release

1. Atualizar versão em `pyproject.toml` e `react_agent_framework/__init__.py`
2. Atualizar `CHANGELOG.md` e `docs/changelog.md` com as mudanças
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
- **MkDocs Material**: Documentação

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

# Servir documentação localmente
mkdocs serve

# Build documentação
mkdocs build
```

## 📦 Instalação e Uso

### Desenvolvimento
```bash
pip install -e ".[dev]"
```

### Com todas as features
```bash
pip install -e ".[all]"
```

### CLI
```bash
react-agent ask "Sua pergunta"
react-agent interactive
```

### API Python
```python
from react_agent_framework import ReactAgent

agent = ReactAgent(
    name="Assistant",
    provider="gpt-4o-mini"
)

@agent.tool()
def search(query: str) -> str:
    """Search for information"""
    return results

answer = agent.run("Your question")
```

## 🚀 Features Implementadas

### ✅ v0.1.0 - Core
- ReactAgent básico
- Padrão ReAct (Reasoning + Acting)
- Integração OpenAI
- CLI com Typer e Rich

### ✅ v0.2.0 - API
- API estilo FastAPI
- Decorador `@agent.tool()`
- Configuração rica

### ✅ v0.3.0 - Multi-Provider
- Suporte OpenAI
- Suporte Anthropic Claude
- Suporte Google Gemini
- Suporte Ollama (local)
- Provider factory

### ✅ v0.4.0 - Built-in Tools
- ToolRegistry
- Método `use_tools()` com pattern matching
- Ferramentas de busca (DuckDuckGo)
- Ferramentas de filesystem (read, write, list, delete)
- Ferramentas de computação (calculator, code executor, shell)

### ✅ v0.5.0 - Memory
- SimpleMemory (em memória)
- ChromaMemory (vector database)
- FAISSMemory (similarity search)
- BaseMemory abstract class

### ✅ v0.6.0 - Objectives
- Sistema de objetivos
- Tracking de progresso
- Níveis de prioridade
- Success criteria
- Integração com ReactAgent

### ✅ v0.7.0 - Reasoning
- ReActReasoning (iterativo)
- ReWOOReasoning (plan-then-execute)
- ReflectionReasoning (self-critique)
- PlanExecuteReasoning (adaptive planning)

### ✅ v0.8.0 - Environments
- WebEnvironment (browser automation)
- CLIEnvironment (shell commands)
- FileEnvironment (file operations)
- Safe mode para todos

### ✅ v0.9.0 - MCP + Docs
- **MCP Integration**:
  - MCPClient (async + sync)
  - MCPToolAdapter
  - MCPConfigManager
  - Suporte a servidores populares
  - Auto-registro de tools
- **Documentação Completa**:
  - Site com Material for MkDocs
  - Getting Started guides
  - Feature documentation
  - API Reference
  - Examples
  - Deploy automático via GitHub Pages

### ✅ v0.10.0 - Memory Refactoring
- **Separação Chat vs Knowledge Memory**:
  - Chat Memory: Histórico de conversação
  - Knowledge Memory: RAG / Semantic Search
  - Interfaces separadas e especializadas
  - Backward compatibility mantida

### ✅ v0.10.1 - Bugfixes
- Correções de compatibilidade de interface
- Melhorias na integração ReactAgent + Memory

### ✅ v0.11.0 - Layer 4: Agentic Infrastructure 🎉
- **Part 1/5: Monitoring System**
  - AgentMetrics (Prometheus export, token tracking, cost tracking)
  - AgentLogger (structured JSON logging, context propagation)
  - AgentTelemetry (distributed tracing, OpenTelemetry-compatible)

- **Part 2/5: Resilience System**
  - RetryStrategy (exponential backoff, jitter, configurable)
  - CircuitBreaker (CLOSED/OPEN/HALF_OPEN states, fault isolation)
  - FallbackStrategy (static, function, chain fallbacks)
  - TimeoutManager (thread-based timeout enforcement)

- **Part 3/5: Security System**
  - RBACManager (20+ permissions, roles, wildcard support)
  - Sandbox (file/network isolation, command whitelist)
  - AuditLogger (compliance logging, structured events)
  - SecretsManager (encrypted storage, expiration, rotation)

- **Part 4/5: Cost Control System**
  - BudgetTracker (multi-period budgets, alerts, projections)
  - RateLimiter (token bucket + sliding window algorithms)
  - QuotaManager (multi-type quotas, auto-reset)

- **Part 5/5: Human-in-the-Loop System**
  - ApprovalManager (6 policies, async approval, callbacks)
  - InterventionManager (real-time intervention, step mode)
  - FeedbackCollector (6 feedback types, analytics, export)

**Total:** 5 sistemas, 15 componentes, ~5500 linhas, 100% thread-safe

## 📚 Documentação

### Estrutura da Documentação

```
docs/
├── index.md                    # Página inicial
├── getting-started/
│   ├── installation.md         # Instalação
│   ├── quickstart.md           # Início rápido (5min)
│   └── first-agent.md          # Primeiro agente completo
├── features/
│   ├── multi-provider.md       # Multi-provider support
│   ├── built-in-tools.md       # Ferramentas built-in
│   ├── memory-systems.md       # Sistemas de memória
│   ├── objectives.md           # Sistema de objetivos
│   ├── reasoning-strategies.md # Estratégias de raciocínio
│   ├── environments.md         # Ambientes
│   └── mcp-integration.md      # Integração MCP
├── guides/
│   ├── custom-tools.md         # Criar ferramentas
│   ├── custom-providers.md     # Criar providers
│   ├── memory-backends.md      # Criar backends de memória
│   └── deployment.md           # Deploy em produção
├── api-reference/              # Referência completa da API
├── examples/                   # Exemplos práticos
├── contributing.md             # Como contribuir
└── changelog.md                # Histórico de mudanças
```

### Deploy da Documentação

- **URL**: https://marcosf63.github.io/react-agent-framework/
- **Deploy**: Automático via GitHub Actions ao fazer push para `main`
- **Tecnologia**: Material for MkDocs
- **Features**: Search, dark mode, navigation tabs, code copy

## 🚀 Roadmap

### v0.12.0 (Próxima versão)
- [ ] Testes unitários com pytest (cobertura >80%)
- [ ] CI/CD completo com GitHub Actions
- [ ] Mais exemplos documentados
- [ ] Documentação para Layer 4 Infrastructure

### v0.13.0+ (Multi-Agent Systems)
- [ ] Layer 3: Multi-Agent communication
- [ ] Orchestration patterns
- [ ] State coordination
- [ ] Agent collaboration protocols

### v1.0.0 (Versão estável)
- [ ] API estável e documentada
- [ ] Cobertura de testes >= 80%
- [ ] CI/CD completo com testes
- [ ] Publicação no PyPI
- [ ] Documentação completa de todas as layers
- [ ] Benchmarks de performance
- [ ] Production deployment guides

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
- **Documentação**: https://marcosf63.github.io/react-agent-framework/
- **Issues**: https://github.com/marcosf63/react-agent-framework/issues
- **PyPI**: https://pypi.org/project/react-agent-framework/ (em breve)

---

Última atualização: 2025-01-11
Versão: 0.11.0 🚀 (Production-Ready)
