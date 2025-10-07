# ReAct Agent Framework

> Framework genérico para criar aplicações com agentes AI usando padrão ReAct (Reasoning + Acting)

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🤖 O que é ReAct?

ReAct (Reasoning + Acting) é um padrão de agente que alterna entre:
- **Pensamento (Reasoning)**: Raciocinar sobre o que fazer
- **Ação (Acting)**: Executar uma ação usando ferramentas disponíveis
- **Observação**: Analisar o resultado da ação

Este ciclo continua até o agente ter informação suficiente para responder.

## 🚀 Funcionalidades

- ✅ Framework extensível e genérico para criar agentes AI
- ✅ Ferramentas built-in (pesquisa web, calculadora)
- ✅ Fácil criação de ferramentas personalizadas
- ✅ CLI interativa com Typer e Rich
- ✅ Modo verbose para debug do raciocínio
- ✅ API Python limpa e intuitiva
- ✅ Instalável via pip
- ✅ TypeHints e documentação completa

## 📋 Pré-requisitos

- Python 3.8+
- Chave de API da OpenAI

## 🔧 Instalação

### Instalação local (desenvolvimento)

```bash
# Clone o repositório
git clone https://github.com/marcos/react-agent-framework.git
cd react-agent-framework

# Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate

# Instale em modo editável
pip install -e .

# Configure a chave da OpenAI
cp .env.example .env
# Edite o arquivo .env e adicione sua OPENAI_API_KEY
```

### Instalação via pip (quando publicado no PyPI)

```bash
pip install react-agent-framework
```

## 💻 Uso

### CLI (Interface de Linha de Comando)

Após a instalação, o comando `react-agent` estará disponível:

**Fazer uma pergunta simples:**
```bash
react-agent perguntar "Qual é a capital da França?"
```

**Modo verbose (mostra o raciocínio):**
```bash
react-agent perguntar "Qual é a capital da França?" --verbose
# ou
react-agent perguntar "Qual é a capital da França?" -v
```

**Modo interativo:**
```bash
react-agent interativo
# ou com verbose
react-agent interativo --verbose
```

**Escolher modelo diferente:**
```bash
react-agent perguntar "Pesquise sobre IA" --modelo gpt-4
```

**Ver versão:**
```bash
react-agent versao
```

**Ajuda:**
```bash
react-agent --help
react-agent perguntar --help
```

### API Python

#### Exemplo básico

```python
from react_agent_framework import AgenteReAct
from react_agent_framework.tools import FerramentaPesquisa, FerramentaCalculadora

# Criar ferramentas
ferramentas = [
    FerramentaPesquisa(),
    FerramentaCalculadora()
]

# Criar agente
agente = AgenteReAct(
    ferramentas=ferramentas,
    modelo="gpt-4o-mini",
    max_iteracoes=10
)

# Fazer uma pergunta
resposta = agente.executar(
    "Qual é a capital da França e quantos habitantes tem?",
    verbose=True
)

print(f"Resposta: {resposta}")
```

#### Criar ferramentas personalizadas

```python
from react_agent_framework import AgenteReAct, Ferramenta
import datetime

class FerramentaData(Ferramenta):
    """Ferramenta que retorna a data atual"""

    def __init__(self):
        super().__init__(
            nome="data_atual",
            descricao="Retorna a data e hora atual"
        )

    def executar(self, entrada: str) -> str:
        agora = datetime.datetime.now()
        return f"Data: {agora.strftime('%d/%m/%Y')}, Hora: {agora.strftime('%H:%M:%S')}"

# Usar com o agente
ferramentas = [FerramentaData()]
agente = AgenteReAct(ferramentas=ferramentas)
resposta = agente.executar("Que horas são?")
```

## 📁 Estrutura do Projeto

```
react-agent-framework/
├── react_agent_framework/      # Pacote principal
│   ├── __init__.py            # Exports públicos
│   ├── core/                  # Core do framework
│   │   ├── __init__.py
│   │   ├── agent.py          # Implementação do agente ReAct
│   │   └── base.py           # Classes base (Ferramenta, etc)
│   ├── tools/                 # Ferramentas built-in
│   │   ├── __init__.py
│   │   ├── search.py         # Ferramenta de pesquisa
│   │   └── calculator.py     # Calculadora
│   ├── cli/                   # Interface CLI
│   │   ├── __init__.py
│   │   └── app.py            # Aplicação Typer
│   └── examples/              # Exemplos de uso
│       ├── __init__.py
│       ├── basic_usage.py
│       └── custom_tool.py
├── pyproject.toml             # Configuração do projeto
├── setup.py                   # Setup alternativo
├── MANIFEST.in               # Arquivos a incluir no pacote
├── LICENSE                    # Licença MIT
├── README.md                  # Este arquivo
└── .env.example              # Exemplo de configuração
```

## 🔍 Como Funciona

1. **Usuário faz uma pergunta** → "Qual é a capital da França?"

2. **Agente pensa** → "Preciso pesquisar sobre a capital da França"

3. **Agente age** → Usa a ferramenta de pesquisa

4. **Agente observa** → Recebe: "Paris é a capital da França..."

5. **Agente pensa** → "Agora tenho a informação necessária"

6. **Agente finaliza** → "A capital da França é Paris"

## 🛠️ Desenvolvimento

### Instalar dependências de desenvolvimento

```bash
pip install -e ".[dev]"
```

### Executar exemplos

```bash
# Exemplo básico
python -m react_agent_framework.examples.basic_usage

# Exemplo com ferramentas personalizadas
python -m react_agent_framework.examples.custom_tool
```

### Rodar testes (quando implementados)

```bash
pytest
pytest --cov=react_agent_framework
```

### Formatação de código

```bash
black react_agent_framework/
ruff check react_agent_framework/
```

## 🎯 Casos de Uso

- 🔍 Pesquisa e análise de informações
- 🧮 Cálculos e processamento de dados
- 🤖 Assistentes virtuais inteligentes
- 📊 Análise e relatórios automatizados
- 🔧 Automação de tarefas complexas
- 💡 Qualquer aplicação que necessite raciocínio + ação

## 📚 Ferramentas Built-in

| Ferramenta | Descrição | Uso |
|-----------|-----------|-----|
| `FerramentaPesquisa` | Pesquisa na internet via DuckDuckGo | Buscar informações online |
| `FerramentaCalculadora` | Calculadora matemática | Realizar cálculos |

## ⚙️ Configuração do Agente

```python
agente = AgenteReAct(
    ferramentas=lista_ferramentas,    # Lista de ferramentas disponíveis
    modelo="gpt-4o-mini",              # Modelo OpenAI (gpt-4o-mini, gpt-4, etc)
    max_iteracoes=10,                  # Máximo de ciclos pensamento-ação
    api_key="sk-..."                   # Chave API (opcional, usa .env)
)
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Fork o repositório
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

### Ideias para contribuição

- Adicionar novas ferramentas built-in
- Melhorar o prompt do agente
- Adicionar suporte a outros LLMs (Anthropic, etc)
- Implementar testes
- Melhorar a documentação
- Criar mais exemplos

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🙏 Agradecimentos

- Inspirado no paper [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- Construído com [OpenAI API](https://openai.com/), [Typer](https://typer.tiangolo.com/) e [Rich](https://rich.readthedocs.io/)

## 📧 Contato

Marcos - marcosf63@gmail.com

---

**Criado com ❤️ usando ReAct Agent Framework**
