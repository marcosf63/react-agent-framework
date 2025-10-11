# 📚 Guia de Exemplos - ReAct Agent Framework

Este guia explica como executar e entender cada exemplo do framework.

## 📋 Índice

1. [MCP Demo](#1-mcp-demo) - Integração com Model Context Protocol
2. [Built-in Tools](#2-built-in-tools) - Ferramentas integradas
3. [Multi-Provider](#3-multi-provider) - Múltiplos provedores LLM
4. [Objectives Demo](#4-objectives-demo) - Sistema de objetivos
5. [Custom Tools](#5-custom-tools) - Criação de ferramentas customizadas
6. [Memory Demo](#6-memory-demo) - Sistema de memória (atualizado v0.10.0)

---

## 1. MCP Demo

**Arquivo**: `react_agent_framework/examples/mcp_demo.py`

### O que demonstra
- Conexão com servidores MCP (Model Context Protocol)
- Uso de ferramentas de servidores externos
- Gerenciamento de múltiplos servidores
- Configuração pré-definida de servidores populares

### Pré-requisitos
```bash
# Instalar dependências MCP
pip install mcp

# Instalar servidor filesystem (Node.js)
npm install -g @modelcontextprotocol/server-filesystem
```

### Como executar
```bash
python react_agent_framework/examples/mcp_demo.py
```

### Exemplos incluídos

#### Exemplo 1: Servidor Filesystem
```python
agent = ReactAgent(name="File Assistant", provider="gpt-4o-mini")

# Conectar ao servidor filesystem
server_id = agent.add_mcp_server(
    command="npx",
    args=["-y", "@modelcontextprotocol/server-filesystem", "/tmp"],
    name="filesystem",
    auto_register=True,
)

# Usar ferramentas do servidor
answer = agent.run("List the files in /tmp directory", verbose=True)
```

#### Exemplo 2: Múltiplos Servidores
```python
# Conectar filesystem
fs_server_id = agent.add_mcp_server(...)

# Poderia conectar GitHub
# github_server_id = agent.add_mcp_server(
#     command="npx",
#     args=["-y", "@modelcontextprotocol/server-github"],
#     env={"GITHUB_TOKEN": "ghp_..."},
#     name="github",
# )

# Listar todos servidores conectados
for server in agent.list_mcp_servers():
    print(f"  - {server['name']} (ID: {server['id']}, Tools: {server['num_tools']})")
```

#### Exemplo 3: Configuração Pré-definida
```python
from react_agent_framework.mcp.config import MCPConfigManager

# Listar servidores populares
for name, desc in MCPConfigManager.list_popular_servers().items():
    print(f"  - {name}: {desc}")

# Usar configuração pré-definida
config_manager = MCPConfigManager()
fs_config = config_manager.get_popular_server("filesystem")

server_id = agent.add_mcp_server(
    command=fs_config.command,
    args=fs_config.args,
    env=fs_config.env,
    name=fs_config.name,
)
```

### Conceitos-chave
- **MCP Server**: Servidor externo que fornece ferramentas
- **Auto-register**: Registra automaticamente todas as ferramentas do servidor
- **Server ID**: Identificador único para gerenciar conexões

---

## 2. Built-in Tools

**Arquivo**: `react_agent_framework/examples/builtin_tools.py`

### O que demonstra
- Ferramentas integradas do framework
- Registro de ferramentas com pattern matching
- Combinação de múltiplas ferramentas

### Como executar
```bash
python react_agent_framework/examples/builtin_tools.py
```

### Exemplos incluídos

#### Exemplo 1: Calculator
```python
agent = ReactAgent(name="Math Assistant", provider="gpt-4o-mini")

# Registrar ferramenta de cálculo
agent.use_tools("computation.calculator")

result = agent.run("What is 25 * 4 + 100 / 2?", verbose=True)
```

#### Exemplo 2: Filesystem
```python
agent = ReactAgent(name="File Assistant", provider="gpt-4o-mini")

# Registrar todas ferramentas de filesystem
agent.use_tools("filesystem.*")

result = agent.run("List all Python files in the current directory", verbose=True)
```

#### Exemplo 3: Search
```python
agent = ReactAgent(name="Search Assistant", provider="gpt-4o-mini")

# Registrar ferramenta de busca
agent.use_tools("search.duckduckgo")

result = agent.run("What is the latest version of Python?", verbose=True)
```

#### Exemplo 4: Múltiplas Ferramentas
```python
agent = ReactAgent(name="Multi-tool Assistant", provider="gpt-4o-mini")

# Registrar várias ferramentas específicas
agent.use_tools(
    "search.duckduckgo",
    "computation.calculator",
    "filesystem.list",
)

result = agent.run(
    "Search for the current Python version, calculate 2024 - 1991, and list current directory",
    verbose=True,
)
```

#### Exemplo 5: Todas as Ferramentas
```python
agent = ReactAgent(name="Super Assistant", provider="gpt-4o-mini")

# Registrar TODAS as ferramentas disponíveis
agent.use_tools("*")

print(f"Registered tools: {', '.join(agent.get_tools().keys())}")
```

### Ferramentas Built-in Disponíveis

**Computation**:
- `computation.calculator` - Calculadora matemática

**Filesystem**:
- `filesystem.read` - Ler arquivo
- `filesystem.write` - Escrever arquivo
- `filesystem.list` - Listar diretório
- `filesystem.delete` - Deletar arquivo

**Search**:
- `search.duckduckgo` - Busca web com DuckDuckGo

### Pattern Matching

```python
# Específico
agent.use_tools("computation.calculator")

# Categoria completa
agent.use_tools("filesystem.*")

# Múltiplas ferramentas
agent.use_tools("search.*", "computation.*")

# Todas
agent.use_tools("*")
```

---

## 3. Multi-Provider

**Arquivo**: `react_agent_framework/examples/multi_provider.py`

### O que demonstra
- Suporte a múltiplos provedores LLM
- Diferentes formas de configuração
- Auto-detecção de provider

### Como executar
```bash
# Configure as API keys necessárias
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."
export GOOGLE_API_KEY="..."

python react_agent_framework/examples/multi_provider.py
```

### Exemplos incluídos

#### Exemplo 1: OpenAI (string simples)
```python
agent = ReactAgent(
    name="OpenAI Assistant",
    provider="gpt-4o-mini"  # String simples, usa OpenAI por padrão
)
```

#### Exemplo 2: OpenAI (URL-style)
```python
agent = ReactAgent(
    name="OpenAI URL Assistant",
    provider="openai://gpt-4o-mini"  # URL-style explícito
)
```

#### Exemplo 3: Anthropic Claude
```python
agent = ReactAgent(
    name="Claude Assistant",
    provider="anthropic://claude-3-5-sonnet-20241022"
)
```

#### Exemplo 4: Provider Object
```python
from react_agent_framework.providers import AnthropicProvider

claude_provider = AnthropicProvider(
    model="claude-3-5-sonnet-20241022",
    # api_key="your-key-here"  # Opcional, usa env
)

agent = ReactAgent(
    name="Claude Object Assistant",
    provider=claude_provider
)
```

#### Exemplo 5: Google Gemini
```python
agent = ReactAgent(
    name="Gemini Assistant",
    provider="google://gemini-1.5-flash"
)
```

#### Exemplo 6: Ollama (Local)
```python
# Requer Ollama rodando localmente
agent = ReactAgent(
    name="Ollama Assistant",
    provider="ollama://llama3.2"
)
```

#### Exemplo 7: Auto-detecção
```python
# Auto-detectado pelo prefixo do modelo
agent_claude = ReactAgent(provider="claude-3-5-sonnet-20241022")  # → Anthropic
agent_gemini = ReactAgent(provider="gemini-1.5-flash")  # → Google
agent_llama = ReactAgent(provider="llama3.2")  # → Ollama
```

### Providers Suportados

| Provider   | URL Format              | Auto-detect Prefix | Requer API Key |
|-----------|-------------------------|-------------------|---------------|
| OpenAI    | `openai://model`        | `gpt-*`          | Sim           |
| Anthropic | `anthropic://model`     | `claude-*`       | Sim           |
| Google    | `google://model`        | `gemini-*`       | Sim           |
| Ollama    | `ollama://model`        | `llama*`         | Não (local)   |

---

## 4. Objectives Demo

**Arquivo**: `react_agent_framework/examples/objectives_demo.py`

### O que demonstra
- Sistema de objetivos para agentes orientados a metas
- Tracking de progresso
- Prioridades e deadlines
- Sub-objetivos e hierarquias
- Persistência de objetivos

### Como executar
```bash
python react_agent_framework/examples/objectives_demo.py
```

### Exemplos incluídos

#### Demo 1: Objetivos Básicos
```python
from react_agent_framework.core.objectives import Objective, ObjectiveTracker

# Criar objetivos
obj1 = Objective(
    goal="Research Python frameworks",
    success_criteria=["Find 3+ frameworks", "Compare features"],
    priority="high",
)

obj2 = Objective(
    goal="Write documentation",
    success_criteria=["Create README", "Add examples"],
    priority="medium",
    deadline=datetime.now() + timedelta(days=7),
)

# Criar tracker
tracker = ObjectiveTracker()
tracker.add(obj1)
tracker.add(obj2)

# Trabalhar no próximo objetivo
next_obj = tracker.start_next()

# Atualizar progresso
tracker.update_progress(next_obj.id, 0.5, "Found 2 frameworks so far")

# Completar
tracker.complete(next_obj.id, "Research completed successfully")
```

#### Demo 2: Agent com Objetivos
```python
objectives = [
    Objective(
        goal="Calculate the total cost of purchasing 15 items at $8.99 each",
        success_criteria=["Perform calculation", "Provide final total"],
        priority="high",
    ),
]

agent = ReactAgent(
    name="Goal-Oriented Assistant",
    provider="gpt-4o-mini",
    objectives=objectives,
)

# Agent executa e pode marcar objetivos como completos
answer = agent.run("Calculate 15 * 8.99", verbose=False)

first_obj = agent.objectives.get_active()[0]
agent.objectives.complete(first_obj.id, "Calculation completed")
```

#### Demo 3: Gerenciamento de Prioridades
```python
tracker = ObjectiveTracker()

# Adicionar com diferentes prioridades
tracker.create(
    goal="Fix critical security bug",
    priority="critical",
    deadline=datetime.now() + timedelta(hours=2),
)

tracker.create(
    goal="Update documentation",
    priority="low",
    deadline=datetime.now() + timedelta(days=30),
)

# Objetivos são processados por prioridade
while tracker.get_pending():
    obj = tracker.start_next()  # Pega o próximo por prioridade
    print(f"Working on: {obj.goal} (priority: {obj.priority.value})")
    tracker.complete(obj.id, f"Completed {obj.goal}")
```

#### Demo 4: Sub-objetivos
```python
# Objetivo principal
main_obj = Objective(
    goal="Build and deploy web application",
    priority="high",
)

# Adicionar sub-objetivos
main_obj.add_sub_objective(
    Objective(goal="Design database schema", priority="high")
)
main_obj.add_sub_objective(
    Objective(goal="Implement API endpoints", priority="high")
)
main_obj.add_sub_objective(
    Objective(goal="Create frontend UI", priority="medium")
)

# Calcular progresso geral
overall_progress = sum(s.progress for s in main_obj.sub_objectives) / len(main_obj.sub_objectives)
```

#### Demo 5: Persistência
```python
# Salvar objetivos
tracker_data = tracker.to_dict()

# Carregar objetivos
new_tracker = ObjectiveTracker.from_dict(tracker_data)
```

### Níveis de Prioridade

1. **critical** - Urgente, deve ser feito imediatamente
2. **high** - Alta prioridade
3. **medium** - Prioridade média
4. **low** - Baixa prioridade

### Conceitos-chave
- **Objective**: Meta com critérios de sucesso
- **ObjectiveTracker**: Gerencia múltiplos objetivos
- **Success Criteria**: Lista de requisitos para completar
- **Sub-objectives**: Objetivos hierárquicos
- **Progress**: Porcentagem de conclusão (0.0 - 1.0)

---

## 5. Custom Tools

**Arquivo**: `react_agent_framework/examples/custom_tools.py`

### O que demonstra
- Criação de ferramentas customizadas com decoradores
- Diferentes tipos de ferramentas
- Registro com nome e descrição personalizados

### Como executar
```bash
python react_agent_framework/examples/custom_tools.py
```

### Exemplos incluídos

#### Ferramenta Simples
```python
agent = ReactAgent(
    name="Personal Assistant",
    provider="gpt-4o-mini",
)

@agent.tool()
def get_datetime() -> str:
    """Get current date and time"""
    now = datetime.now()
    return f"Date: {now.strftime('%Y-%m-%d')}, Time: {now.strftime('%H:%M:%S')}"
```

#### Ferramenta com Parâmetros
```python
@agent.tool()
def random_number(range_str: str) -> str:
    """Generate random number. Input format: 'min-max' (e.g., '1-100')"""
    min_val, max_val = map(int, range_str.split("-"))
    number = random.randint(min_val, max_val)
    return f"Random number between {min_val} and {max_val}: {number}"
```

#### Ferramenta Complexa
```python
@agent.tool()
def convert_temperature(input_str: str) -> str:
    """Convert temperature. Format: 'C to F: 25' or 'F to C: 77'"""
    if "C to F" in input_str:
        celsius = float(input_str.split(":")[-1].strip())
        fahrenheit = (celsius * 9 / 5) + 32
        return f"{celsius}°C = {fahrenheit}°F"

    elif "F to C" in input_str:
        fahrenheit = float(input_str.split(":")[-1].strip())
        celsius = (fahrenheit - 32) * 5 / 9
        return f"{fahrenheit}°F = {celsius:.2f}°C"
```

#### Ferramenta com Nome Customizado
```python
@agent.tool(name="greet", description="Greet someone by name")
def greet_person(name: str) -> str:
    """Custom greeting"""
    return f"Hello, {name}! How can I assist you today?"
```

### Uso das Ferramentas

```python
# Listar ferramentas registradas
for tool_name, tool_desc in agent.get_tools().items():
    print(f"  - {tool_name}: {tool_desc}")

# Usar ferramenta via pergunta natural
answer = agent.run("What time is it now?", verbose=True)
answer = agent.run("Generate a random number between 1 and 100", verbose=True)
answer = agent.run("Convert 25 degrees Celsius to Fahrenheit", verbose=True)
answer = agent.run("Greet John", verbose=True)
```

### Boas Práticas

1. **Docstrings claras**: Sempre documente o que a ferramenta faz
2. **Type hints**: Use type hints para parâmetros e retorno
3. **Error handling**: Trate erros adequadamente
4. **Formato de entrada**: Documente formato esperado de parâmetros
5. **Retorno consistente**: Sempre retorne string

---

## 6. Memory Demo

**Arquivo**: `react_agent_framework/examples/memory_demo.py`

### O que demonstra
Sistema de memória v0.10.0 completamente refatorado:
- **Chat Memory**: Histórico de conversação (SQLite, in-memory)
- **Knowledge Memory**: Base de conhecimento para RAG (ChromaDB, FAISS)

### Como executar
```bash
# Memória básica (sem dependências extras)
python react_agent_framework/examples/memory_demo.py

# Com ChromaDB
pip install chromadb
python react_agent_framework/examples/memory_demo.py

# Com FAISS
pip install faiss-cpu sentence-transformers
python react_agent_framework/examples/memory_demo.py
```

### Demos Incluídas

#### Demo 1: SimpleChatMemory (In-Memory)
```python
from react_agent_framework.core.memory import SimpleChatMemory

# Criar memória de chat em memória
memory = SimpleChatMemory(
    session_id="demo-session",
    max_messages=100
)

# Adicionar mensagens
memory.add_message("Hello!", role="user")
memory.add_message("Hi there!", role="assistant")

# Buscar histórico
history = memory.get_history(limit=10)
for msg in history:
    print(f"[{msg.role}]: {msg.content}")

# Limpar sessão
memory.clear()
```

#### Demo 2: SQLiteChatMemory (Persistente) ⭐ NOVO!
```python
from react_agent_framework.core.memory import SQLiteChatMemory

# Criar memória persistente (SQLite)
memory = SQLiteChatMemory(
    db_path="./chat_memory.db",
    session_id="persistent-session",
    max_messages=1000,
    auto_vacuum=True
)

# Adicionar conversação
memory.add_message("What is Python?", role="user")
memory.add_message("Python is a programming language", role="assistant")

# Buscar histórico (persiste entre execuções!)
history = memory.get_history(session_id="persistent-session")

# Multi-sessão
memory.switch_session("another-session")
memory.add_message("Different conversation", role="user")

# Buscar por sessão
session1_history = memory.get_history(session_id="persistent-session")
session2_history = memory.get_history(session_id="another-session")
```

#### Demo 3: ChromaKnowledgeMemory (RAG)
```python
from react_agent_framework.core.memory import ChromaKnowledgeMemory

# Criar base de conhecimento com ChromaDB
knowledge = ChromaKnowledgeMemory(
    collection_name="python_docs",
    persist_directory="./chroma_db"
)

# Adicionar documentos
knowledge.add_document(
    content="Python is a high-level programming language known for simplicity",
    metadata={"topic": "python", "type": "definition"}
)

knowledge.add_document(
    content="FastAPI is a modern web framework for building APIs with Python",
    metadata={"topic": "fastapi", "type": "framework"}
)

# Buscar semanticamente (RAG)
results = knowledge.search(
    query="What web frameworks exist for Python?",
    top_k=3,
    filters={"type": "framework"}
)

for doc in results:
    print(f"Score: {doc.score:.3f}")
    print(f"Content: {doc.content}")
    print(f"Metadata: {doc.metadata}")
```

#### Demo 4: FAISSKnowledgeMemory (High-Performance)
```python
from react_agent_framework.core.memory import FAISSKnowledgeMemory

# Criar base de conhecimento com FAISS (rápido!)
knowledge = FAISSKnowledgeMemory(
    index_path="./faiss_index",
    embedding_model="all-MiniLM-L6-v2"
)

# Adicionar documentos
doc_ids = []
for i in range(100):
    doc_id = knowledge.add_document(
        content=f"Document {i} about AI and machine learning",
        metadata={"doc_num": i}
    )
    doc_ids.append(doc_id)

# Busca rápida em grande volume
results = knowledge.search(
    query="Tell me about AI",
    top_k=5
)

# FAISS é otimizado para grandes volumes (>10k documentos)
```

#### Demo 5: Memória Combinada (Chat + Knowledge) ⭐ NOVO!
```python
from react_agent_framework import ReactAgent
from react_agent_framework.core.memory import SQLiteChatMemory, ChromaKnowledgeMemory

# Criar agent com ambos os tipos de memória
chat_memory = SQLiteChatMemory(db_path="./agent_chat.db")
knowledge_memory = ChromaKnowledgeMemory(collection_name="agent_kb")

agent = ReactAgent(
    name="Smart Assistant",
    provider="gpt-4o-mini",
    memory=chat_memory  # Chat memory no agent
)

# Adicionar conhecimento manualmente
knowledge_memory.add_document(
    "The React Agent Framework uses the ReAct pattern",
    metadata={"source": "docs"}
)

# Usar ambos: chat guarda conversa, knowledge fornece contexto
def ask_with_context(question: str):
    # 1. Buscar contexto relevante
    context_docs = knowledge_memory.search(question, top_k=3)
    context = "\n".join([d.content for d in context_docs])

    # 2. Fazer pergunta com contexto
    prompt = f"Context:\n{context}\n\nQuestion: {question}"
    answer = agent.run(prompt)

    # 3. Chat history é automaticamente salvo
    return answer

answer = ask_with_context("What pattern does the framework use?")
```

#### Demo 6: Comparação e Casos de Uso ⭐ NOVO!
```python
print("=" * 80)
print("QUANDO USAR CADA TIPO DE MEMÓRIA")
print("=" * 80)

print("\n📝 CHAT MEMORY (Histórico de Conversação)")
print("-" * 80)
print("USE QUANDO:")
print("  ✓ Precisa lembrar conversas anteriores")
print("  ✓ Quer manter contexto entre perguntas")
print("  ✓ Precisa de histórico sequencial")
print("  ✓ Trabalha com múltiplas sessões/usuários")
print("\nOPÇÕES:")
print("  • SimpleChatMemory: Teste/desenvolvimento (em memória)")
print("  • SQLiteChatMemory: Produção (persistente, sem deps extras)")
print("\nEXEMPLO:")
print("  Chatbot, assistente conversacional, suporte ao cliente")

print("\n\n📚 KNOWLEDGE MEMORY (Base de Conhecimento RAG)")
print("-" * 80)
print("USE QUANDO:")
print("  ✓ Precisa buscar informação relevante")
print("  ✓ Trabalha com documentos/conhecimento")
print("  ✓ Quer busca semântica (não exata)")
print("  ✓ Implementa RAG (Retrieval Augmented Generation)")
print("\nOPÇÕES:")
print("  • ChromaKnowledgeMemory: Até ~100k docs, recursos avançados")
print("  • FAISSKnowledgeMemory: +100k docs, máxima performance")
print("\nEXEMPLO:")
print("  Sistema de Q&A sobre docs, search engine, recomendação")

print("\n\n🔄 COMBINADO (Chat + Knowledge)")
print("-" * 80)
print("USE QUANDO:")
print("  ✓ Precisa de AMBOS: conversa + conhecimento")
print("  ✓ Quer contexto de docs em conversas")
print("  ✓ Implementa assistente com base de conhecimento")
print("\nCONFIGURAÇÃO:")
print("  • Chat Memory no agent (histórico)")
print("  • Knowledge Memory separado (contexto)")
print("  • Busca contexto → adiciona ao prompt → salva conversa")
print("\nEXEMPLO:")
print("  Assistente técnico com docs, suporte com KB, tutor com materiais")
```

### Conceitos v0.10.0

#### Chat Memory (Conversação)
- **Propósito**: Histórico sequencial de mensagens
- **Armazenamento**: SQL (SQLite, PostgreSQL)
- **Casos de uso**: Chatbots, assistentes, suporte
- **Características**: Sessões, ordem cronológica, limites

#### Knowledge Memory (RAG)
- **Propósito**: Base de conhecimento para busca semântica
- **Armazenamento**: Vetores (ChromaDB, FAISS)
- **Casos de uso**: Q&A, documentação, recomendação
- **Características**: Embeddings, similarity search, metadata

### Migração de v0.9.x

```python
# ❌ ANTIGO (v0.9.x)
from react_agent_framework.core.memory import ChromaMemory

memory = ChromaMemory()  # Era usado para chat (incorreto!)
memory.add("Hello", role="user")

# ✅ NOVO (v0.10.0)

# Para CHAT (conversa):
from react_agent_framework.core.memory import SQLiteChatMemory

chat = SQLiteChatMemory(db_path="./chat.db")
chat.add_message("Hello", role="user")

# Para KNOWLEDGE (documentos/RAG):
from react_agent_framework.core.memory import ChromaKnowledgeMemory

knowledge = ChromaKnowledgeMemory(collection_name="docs")
knowledge.add_document("Python is a language", metadata={"topic": "python"})
results = knowledge.search("What is Python?", top_k=5)
```

---

## 🚀 Dicas Gerais

### Verbose Mode
Use `verbose=True` para ver o raciocínio do agent:
```python
answer = agent.run("Your question", verbose=True)
# Mostra: Thought → Action → Observation → ... → Final Answer
```

### Limpar Histórico
```python
agent.clear_history()  # Limpa histórico de conversação
```

### Verificar Ferramentas
```python
tools = agent.get_tools()
for name, description in tools.items():
    print(f"{name}: {description}")
```

### Configurar Temperature
```python
agent = ReactAgent(
    provider="gpt-4o-mini",
    temperature=0  # 0 = determinístico, 1 = criativo
)
```

---

## 📝 Troubleshooting

### Problema: "API key not found"
**Solução**: Configure as variáveis de ambiente
```bash
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."
export GOOGLE_API_KEY="..."
```

### Problema: "MCP server not found"
**Solução**: Instale as dependências do servidor
```bash
pip install mcp
npm install -g @modelcontextprotocol/server-filesystem
```

### Problema: "ChromaDB not installed"
**Solução**: Instale as dependências opcionais
```bash
pip install chromadb  # Para ChromaKnowledgeMemory
pip install faiss-cpu sentence-transformers  # Para FAISSKnowledgeMemory
```

### Problema: "Memory v0.9.x não funciona"
**Solução**: Veja o [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md) para atualizar para v0.10.0

---

## 📚 Próximos Passos

1. **Leia a documentação completa**: https://marcosf63.github.io/react-agent-framework/
2. **Explore os exemplos**: Rode cada exemplo e veja o output
3. **Modifique os exemplos**: Experimente diferentes parâmetros
4. **Crie seus próprios agents**: Use os exemplos como base
5. **Contribua**: https://github.com/marcosf63/react-agent-framework

---

**Versão**: 0.10.0
**Última atualização**: 2025-01-07
