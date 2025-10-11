# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [0.11.0] - 2025-01-11

### 🚀 Nova Feature: Layer 4 - Agentic Infrastructure

**Implementação completa da camada de infraestrutura para agentes production-ready**

Esta release implementa a **Layer 4** do framework Agentic AI, adicionando componentes essenciais para produção:

#### 📊 Part 1/5: Monitoring System

**Componentes:**
- **AgentMetrics**: Sistema de métricas com suporte Prometheus
  - Contadores thread-safe para execuções, erros, tokens
  - Export em formato Prometheus
  - Tracking de custo e duração
  - Context manager para tracking automático

- **AgentLogger**: Sistema de logging estruturado
  - Formato JSON para ingestão em sistemas de observabilidade
  - Níveis configuráveis (DEBUG, INFO, WARNING, ERROR, CRITICAL)
  - Propagação de contexto entre operações
  - Suporte a file e console output

- **AgentTelemetry**: Sistema de rastreamento distribuído
  - Criação de traces e spans
  - Tracking de duração e status
  - Compatível com OpenTelemetry
  - Propagação de trace_id entre componentes

**Arquivos:**
- `react_agent_framework/infrastructure/monitoring/metrics.py` (290 linhas)
- `react_agent_framework/infrastructure/monitoring/logger.py` (248 linhas)
- `react_agent_framework/infrastructure/monitoring/telemetry.py` (244 linhas)
- `react_agent_framework/examples/infrastructure_monitoring_demo.py` (189 linhas)

#### 🛡️ Part 2/5: Resilience System

**Componentes:**
- **RetryStrategy**: Sistema de retry automático
  - Estratégias: Fixed, Exponential, Linear backoff
  - Jitter para prevenir thundering herd
  - Max attempts e delay configuráveis
  - Filtro de exceções retryable

- **CircuitBreaker**: Proteção contra falhas em cascata
  - Estados: CLOSED, OPEN, HALF_OPEN
  - Transição automática baseada em threshold
  - Recovery timeout configurável
  - Métricas de falhas e sucessos

- **FallbackStrategy**: Estratégias de degradação graceful
  - Static fallback (valor fixo)
  - Function fallback (função alternativa)
  - Chain fallback (múltiplas alternativas)
  - Preservação de argumentos originais

- **TimeoutManager**: Gerenciamento de timeouts
  - Timeout configurável por operação
  - Thread-based timeout enforcement
  - Context manager para uso fácil
  - Cleanup automático de threads

**Arquivos:**
- `react_agent_framework/infrastructure/resilience/retry.py` (252 linhas)
- `react_agent_framework/infrastructure/resilience/circuit_breaker.py` (287 linhas)
- `react_agent_framework/infrastructure/resilience/fallback.py` (220 linhas)
- `react_agent_framework/infrastructure/resilience/timeout.py` (212 linhas)
- `react_agent_framework/examples/infrastructure_resilience_demo.py` (259 linhas)

#### 🔒 Part 3/5: Security System

**Componentes:**
- **RBACManager**: Role-Based Access Control
  - 20+ permissions predefinidas
  - Roles: user, developer, admin, auditor
  - Wildcard support (tool.*, file.*)
  - Permission inheritance

- **Sandbox**: Ambiente de execução isolado
  - File system isolation
  - Network access control
  - Command whitelist/blacklist
  - Path resolution e validation

- **AuditLogger**: Sistema de auditoria completo
  - Níveis: INFO, WARNING, SECURITY, COMPLIANCE
  - Formato JSON estruturado
  - File e console output
  - Retenção de logs configurável

- **SecretsManager**: Gerenciamento de segredos
  - Armazenamento criptografado
  - Expiração de segredos
  - Rotation support
  - Environment variables integration

**Arquivos:**
- `react_agent_framework/infrastructure/security/permissions.py` (373 linhas)
- `react_agent_framework/infrastructure/security/sandbox.py` (336 linhas)
- `react_agent_framework/infrastructure/security/audit.py` (367 linhas)
- `react_agent_framework/infrastructure/security/secrets.py` (342 linhas)
- `react_agent_framework/examples/infrastructure_security_demo.py` (320 linhas)

#### 💰 Part 4/5: Cost Control System

**Componentes:**
- **BudgetTracker**: Tracking de orçamento multi-período
  - Períodos: Hourly, Daily, Weekly, Monthly
  - Gastos por categoria
  - Alert thresholds (soft/hard limits)
  - Projeção de custos
  - Relatórios detalhados

- **RateLimiter**: Rate limiting com múltiplos algoritmos
  - Token Bucket (com burst support)
  - Sliding Window
  - Per-user rate limiting
  - Wait time calculation
  - Estatísticas de uso

- **QuotaManager**: Gerenciamento de quotas de recursos
  - Tipos: Requests, Tokens, Storage, Executions, API calls
  - Reset automático por período
  - Per-user e global quotas
  - Warning thresholds
  - Usage reporting

**Arquivos:**
- `react_agent_framework/infrastructure/cost_control/budget.py` (400+ linhas)
- `react_agent_framework/infrastructure/cost_control/rate_limiter.py` (350+ linhas)
- `react_agent_framework/infrastructure/cost_control/quota.py` (380+ linhas)
- `react_agent_framework/examples/infrastructure_cost_control_demo.py` (520+ linhas)

#### 👤 Part 5/5: Human-in-the-Loop System

**Componentes:**
- **ApprovalManager**: Sistema de aprovação de workflows
  - Políticas: ALWAYS, NEVER, COST_THRESHOLD, RISK_LEVEL, FIRST_TIME, CUSTOM
  - Auto-approval baseado em regras
  - Async approval com callbacks
  - Request expiration
  - Approval history e audit trail

- **InterventionManager**: Mecanismos de intervenção humana
  - Tipos: PAUSE, STOP, MODIFY, SKIP, CONTINUE, REDIRECT
  - Intervention points configuráveis
  - Step-by-step execution mode
  - Global pause/resume
  - Real-time parameter modification

- **FeedbackCollector**: Coleta e análise de feedback
  - Tipos: Rating (1-5), Thumbs up/down, Comment, Correction, Bug report, Feature request
  - Agregação de ratings
  - Thumbs statistics
  - Correction tracking
  - Acknowledgment system
  - Export de dados

**Arquivos:**
- `react_agent_framework/infrastructure/human_loop/approval.py` (450+ linhas)
- `react_agent_framework/infrastructure/human_loop/intervention.py` (420+ linhas)
- `react_agent_framework/infrastructure/human_loop/feedback.py` (500+ linhas)
- `react_agent_framework/examples/infrastructure_human_loop_demo.py` (550+ linhas)

### 📈 Estatísticas da Release

- **Total de arquivos novos**: 20
- **Total de linhas de código**: ~5500 linhas
- **Componentes implementados**: 15
- **Demos criados**: 5

### 🎯 Completude do Framework

Com esta release, o framework atinge os seguintes níveis de completude nas 4 camadas do Agentic AI:

- **Layer 1 (LLMs)**: 90% ✅
- **Layer 2 (AI Agents)**: 85% ✅
- **Layer 3 (Multi-Agent Systems)**: 5%
- **Layer 4 (Agentic Infrastructure)**: 100% ✅✅✅

### 🔧 Técnico

- Todas as implementações são **thread-safe**
- Suporte a **configuração flexível** via parâmetros
- **Error handling** abrangente
- **Type hints** completos
- Demos **executáveis** e documentados
- Padrões de design **production-ready**

### 📝 Breaking Changes

Esta release **NÃO introduz breaking changes**. Toda a infraestrutura é opt-in e pode ser adicionada a agentes existentes sem modificar código.

### ⚡ Próximos Passos (v0.12.0+)

- Testes unitários completos (pytest)
- CI/CD pipeline
- Layer 3: Multi-Agent Systems
- Publicação no PyPI

---

## [0.10.1] - 2025-01-11

### 🐛 Correções

- **Interface BaseChatMemory**: Melhorado método `get_context()` para suportar parâmetros compatíveis com ReactAgent
  - Adicionado parâmetro `query` (busca com palavra-chave opcional)
  - Adicionado parâmetro `max_tokens` (limite de tokens no contexto)
  - Adicionado parâmetro `use_search` (ativar/desativar busca)
  - Mantida retrocompatibilidade com `max_messages`

- **ReactAgent**: Suporte completo para ambas interfaces de memória
  - Aceita `BaseMemory` (interface antiga/legada)
  - Aceita `BaseChatMemory` (interface nova v0.10.0)
  - Conversão automática via `ChatToLegacyAdapter` quando necessário
  - Type hints atualizados: `Union[BaseMemory, BaseChatMemory]`

- **Imports**: Adicionados imports necessários em `ReactAgent`
  - `BaseChatMemory` para type checking
  - `ChatToLegacyAdapter` para conversão automática

### 📝 Documentação

- Melhorada documentação do parâmetro `memory` em `ReactAgent.__init__()`
- Explicação clara sobre suporte a ambas interfaces

### 🔧 Técnico

Esta é uma versão PATCH (bugfix) que corrige incompatibilidades de interface sem quebrar código existente.
Mantém 100% de retrocompatibilidade com v0.10.0 e v0.9.x.

## [0.10.0] - 2025-01-10

### 🎯 BREAKING CHANGES

**Refatoração completa do sistema de memória** - Separação conceitual entre Chat Memory e Knowledge Memory

#### ⚠️ Mudanças na API

**Antes (v0.9.x):**
```python
from react_agent_framework import ReactAgent
from react_agent_framework.core.memory import SimpleMemory

agent = ReactAgent(memory=SimpleMemory())
```

**Agora (v0.10.0):**
```python
from react_agent_framework import ReactAgent
from react_agent_framework.core.memory.chat import SimpleChatMemory

agent = ReactAgent(chat_memory=SimpleChatMemory())
```

### Adicionado

- **Chat Memory System**: Sistema de memória para histórico de conversações
  - `SimpleChatMemory`: Buffer em memória (sem persistência)
  - `SQLiteChatMemory`: Banco SQLite para histórico persistente (**NOVO!**)
  - Suporte multi-sessão
  - Busca por palavra-chave
  - Sem dependências externas (usa stdlib)

- **Knowledge Memory System**: Sistema de memória para RAG/busca semântica
  - `ChromaKnowledgeMemory`: ChromaDB para busca vetorial
  - `FAISSKnowledgeMemory`: FAISS para alta performance
  - API específica para documentos
  - Busca semântica otimizada
  - Metadados e filtros avançados

- **Adapters**: Compatibilidade retroativa
  - `LegacyMemoryAdapter`: Usa BaseMemory como ChatMemory
  - `ChatToLegacyAdapter`: Usa ChatMemory como BaseMemory
  - Código antigo continua funcionando!

- **Documentação**:
  - `MIGRATION_GUIDE.md`: Guia completo de migração
  - Exemplos de uso dos dois tipos de memória
  - Comparativo entre Chat e Knowledge Memory

### Alterado

- **Estrutura de Diretórios**:
  ```
  memory/
  ├── chat/           # Chat Memory (NOVO)
  ├── knowledge/      # Knowledge Memory (NOVO)
  ├── adapters.py     # Compatibilidade (NOVO)
  ├── base.py         # Legacy (mantido)
  ├── simple.py       # Legacy (mantido)
  ├── chroma.py       # Legacy (mantido)
  └── faiss.py        # Legacy (mantido)
  ```

- **pyproject.toml**: Novas dependências opcionais
  - `chat-sqlite`: SQLite (stdlib, sem deps)
  - `chat-postgres`: PostgreSQL (futuro)
  - `knowledge-chroma`: ChromaDB
  - `knowledge-faiss`: FAISS
  - Mantidos: `memory-chroma`, `memory-faiss` (legacy)

- **Versão**: 0.9.1 → 0.10.0 (MINOR - nova funcionalidade)

### Corrigido

- **Separação conceitual correta**:
  - Chat Memory: histórico conversacional sequencial
  - Knowledge Memory: busca vetorial para RAG
  - Antes: ChromaDB/FAISS usados para chat (incorreto)
  - Agora: ChromaDB/FAISS exclusivos para RAG (correto)

### Migração

Consulte [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md) para instruções detalhadas.

**Compatibilidade retroativa garantida** - Código antigo continua funcionando via adapters!

## [0.9.1] - 2025-10-08

### Adicionado
- **Unit Tests**: 77 testes unitários com 100% de taxa de sucesso
  - Testes de imports e exports
  - Testes de providers (OpenAI, Ollama, factory)
  - Testes de sistema de memória (SimpleMemory)
  - Cobertura de código: 25% (focado em módulos core)
- **CI/CD**: GitHub Actions workflows completos
  - Testes automatizados em Ubuntu, Windows e macOS
  - Matriz de Python 3.9, 3.10, 3.11 e 3.12
  - Publicação automática no PyPI via tags
  - Badge de status dos testes no README
- **Test Configuration**: pytest, coverage e fixtures compartilhadas
- **Documentation**: TESTING.md com guia completo de testes e CI/CD

### Corrigido
- Importação de FAISS com numpy (TYPE_CHECKING)
- Importação de MCP client (erro movido para connect_server)
- Exports faltantes em __init__.py (Objective, Memory classes)
- Testes de provider factory com mocks corretos

### Alterado
- **Python 3.8 removido**: Versão mínima agora é Python 3.9+
  - Python 3.8 EOL em outubro de 2024
  - Incompatibilidade com type hints modernos (tuple[...])
- Badge do Python atualizado para 3.9+

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
