# Documentação ReAct Agent Framework

Esta pasta contém a documentação completa do framework usando Material for MkDocs.

## Desenvolvimento Local

### Instalar Dependências

```bash
pip install -r requirements-docs.txt
```

### Servir Localmente

```bash
mkdocs serve
```

Acesse: http://localhost:8000

### Build

```bash
mkdocs build
```

O site será gerado em `site/`.

## Deploy

O deploy é automático via GitHub Actions quando há push para `main`.

URL: https://marcosf63.github.io/react-agent-framework/

## Estrutura

```
docs/
├── index.md                 # Página inicial
├── getting-started/         # Guias de início
├── features/                # Documentação de features
├── guides/                  # Guias práticos
├── api-reference/           # Referência da API
├── examples/                # Exemplos
├── contributing.md          # Como contribuir
└── changelog.md             # Histórico de mudanças
```

## Adicionar Páginas

1. Crie o arquivo `.md` na pasta apropriada
2. Adicione ao `nav` em `mkdocs.yml`
3. Use features do Material for MkDocs (admonitions, tabs, etc.)

## Recursos

- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [MkDocs](https://www.mkdocs.org/)
- [Markdown Guide](https://www.markdownguide.org/)
