# Contributing

Thank you for your interest in contributing to ReAct Agent Framework!

---

## How to Contribute

### Report Bugs

Found a bug? [Open an issue](https://github.com/marcosf63/react-agent-framework/issues) with:

- Clear description
- Steps to reproduce
- Expected vs actual behavior
- Python version and environment

### Suggest Features

Have an idea? [Open an issue](https://github.com/marcosf63/react-agent-framework/issues) with:

- Feature description
- Use case
- Proposed implementation (optional)

### Submit Code

1. Fork the repository
2. Create a branch (`git checkout -b feature/MyFeature`)
3. Make your changes
4. Run tests and linting
5. Commit (`git commit -m 'Add MyFeature'`)
6. Push (`git push origin feature/MyFeature`)
7. Open a Pull Request

---

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/react-agent-framework.git
cd react-agent-framework

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install in editable mode with dev dependencies
pip install -e ".[dev]"
```

---

## Code Quality

### Format Code

```bash
black react_agent_framework/
```

### Lint Code

```bash
ruff check react_agent_framework/
```

### Type Check

```bash
mypy react_agent_framework/ --ignore-missing-imports
```

---

## Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation
- `refactor:` Code refactoring
- `test:` Tests
- `chore:` Maintenance

Example:
```
feat: add support for Google Gemini provider

Adds GoogleProvider class with proper integration
```

---

## Pull Request Guidelines

- Keep PRs focused on a single feature/fix
- Add tests for new features
- Update documentation
- Ensure CI passes
- Link related issues

---

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
