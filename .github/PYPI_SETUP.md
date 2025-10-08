# Configuração de Publicação Automática no PyPI

Este repositório está configurado para publicar automaticamente no PyPI quando uma nova tag de versão é criada.

## 🔧 Configuração Inicial (Uma Vez)

### 1. Criar API Tokens no PyPI

#### PyPI (Produção)
1. Acesse: https://pypi.org/manage/account/token/
2. Clique em "Add API token"
3. Nome: `GitHub Actions - react-agent-framework`
4. Scope: `Project: react-agent-framework`
5. Copie o token gerado (começa com `pypi-`)

#### Test PyPI (Opcional, para testes)
1. Acesse: https://test.pypi.org/manage/account/token/
2. Clique em "Add API token"
3. Nome: `GitHub Actions - react-agent-framework`
4. Scope: `Project: react-agent-framework`
5. Copie o token gerado

### 2. Adicionar Secrets no GitHub

1. Vá em: https://github.com/marcosf63/react-agent-framework/settings/secrets/actions
2. Clique em "New repository secret"
3. Adicione os seguintes secrets:

   **PYPI_API_TOKEN**
   - Name: `PYPI_API_TOKEN`
   - Secret: Cole o token do PyPI (produção)

   **TEST_PYPI_API_TOKEN** (opcional)
   - Name: `TEST_PYPI_API_TOKEN`
   - Secret: Cole o token do Test PyPI

## 🚀 Como Publicar uma Nova Versão

### Método 1: Linha de Comando (Recomendado)

```bash
# 1. Atualizar versão no pyproject.toml
# Edite manualmente ou use um script

# 2. Atualizar CHANGELOG.md
# Adicione as mudanças da nova versão

# 3. Commit das mudanças
git add pyproject.toml CHANGELOG.md
git commit -m "chore: bump version to 0.9.1"
git push origin main

# 4. Criar e push da tag
git tag -a v0.9.1 -m "Release v0.9.1 - Bug fixes and improvements"
git push origin v0.9.1

# ✅ O GitHub Actions vai automaticamente:
# - Construir o pacote
# - Validar com twine
# - Publicar no Test PyPI
# - Publicar no PyPI
# - Criar GitHub Release
```

### Método 2: Interface do GitHub

1. Vá em: https://github.com/marcosf63/react-agent-framework/releases/new
2. Clique em "Choose a tag"
3. Digite a nova versão (ex: `v0.9.1`) e clique "Create new tag"
4. Preencha o título e descrição
5. Clique em "Publish release"

## 📋 Checklist Antes de Publicar

- [ ] Versão atualizada em `pyproject.toml`
- [ ] CHANGELOG.md atualizado com as mudanças
- [ ] Todos os testes passando localmente
- [ ] Código committed e pushed para `main`
- [ ] Tag segue o padrão semver: `v{MAJOR}.{MINOR}.{PATCH}`

## 🔍 Verificar Status da Publicação

1. **Actions Tab**: https://github.com/marcosf63/react-agent-framework/actions
   - Veja o progresso em tempo real
   - Verifique logs se houver erro

2. **PyPI**: https://pypi.org/project/react-agent-framework/
   - Verifique se a nova versão aparece

3. **GitHub Releases**: https://github.com/marcosf63/react-agent-framework/releases
   - Release criado automaticamente

## ❌ Troubleshooting

### Erro: "Version mismatch"
- Certifique-se que a versão em `pyproject.toml` corresponde à tag
- Tag `v0.9.1` deve corresponder a `version = "0.9.1"` no pyproject.toml

### Erro: "File already exists"
- Não é possível republicar a mesma versão
- Incremente a versão e crie uma nova tag

### Erro: "Invalid API token"
- Verifique se o secret `PYPI_API_TOKEN` está configurado corretamente
- Certifique-se que o token não expirou

## 🔄 Workflow Automático

Quando você faz `git push origin v0.9.1`:

1. ✅ GitHub Actions detecta a tag
2. ✅ Extrai a versão da tag
3. ✅ Verifica se corresponde ao pyproject.toml
4. ✅ Instala dependências de build
5. ✅ Constrói o pacote (wheel + sdist)
6. ✅ Valida com `twine check`
7. ✅ Publica no Test PyPI (opcional)
8. ✅ Publica no PyPI
9. ✅ Cria GitHub Release com arquivos

## 📦 Versionamento Semântico

Siga [Semantic Versioning](https://semver.org/):

- **MAJOR** (1.0.0): Mudanças incompatíveis na API
- **MINOR** (0.1.0): Nova funcionalidade compatível
- **PATCH** (0.0.1): Correções de bugs

Exemplos:
- Bug fix: `0.9.0` → `0.9.1`
- Nova feature: `0.9.1` → `0.10.0`
- Breaking change: `0.10.0` → `1.0.0`

## 🎯 Exemplo Completo

```bash
# Corrigir um bug
vim react_agent_framework/core/react_agent.py

# Atualizar versão
vim pyproject.toml  # 0.9.0 → 0.9.1

# Atualizar changelog
vim CHANGELOG.md

# Commit
git add .
git commit -m "fix: resolve memory leak in agent cleanup"
git push origin main

# Criar tag e publicar
git tag -a v0.9.1 -m "Release v0.9.1 - Fix memory leak"
git push origin v0.9.1

# Aguarde ~2 minutos
# ✅ Pacote publicado automaticamente no PyPI!
```

## 🔗 Links Úteis

- [PyPI Package](https://pypi.org/project/react-agent-framework/)
- [Test PyPI](https://test.pypi.org/project/react-agent-framework/)
- [GitHub Actions](https://github.com/marcosf63/react-agent-framework/actions)
- [GitHub Releases](https://github.com/marcosf63/react-agent-framework/releases)
