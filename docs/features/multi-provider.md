# Multi-Provider Support

ReAct Agent Framework supports multiple AI providers, allowing you to switch between OpenAI, Anthropic, Google, and Ollama seamlessly.

## Supported Providers

### OpenAI (Default)

```python
agent = ReactAgent(provider="gpt-4o-mini")
agent = ReactAgent(provider="gpt-4")
```

### Anthropic Claude

```python
agent = ReactAgent(provider="anthropic://claude-3-5-sonnet-20241022")
agent = ReactAgent(provider="anthropic://claude-3-opus-20240229")
```

### Google Gemini

```python
agent = ReactAgent(provider="google://gemini-1.5-flash")
agent = ReactAgent(provider="google://gemini-1.5-pro")
```

### Ollama (Local)

```python
agent = ReactAgent(provider="ollama://llama3.2")
agent = ReactAgent(provider="ollama://mistral")
```

## Configuration

Set API keys in `.env`:

```env
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GOOGLE_API_KEY=AI...
```

## Learn More

See [API Reference](../api-reference/providers.md) for details.
