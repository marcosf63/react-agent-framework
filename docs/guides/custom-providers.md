# Custom LLM Providers

The ReAct Agent Framework supports multiple LLM providers out of the box and makes it easy to create your own custom providers. This guide covers both using built-in providers and creating custom ones.

## Built-in Providers

The framework includes support for:

- **OpenAI** - GPT-4, GPT-3.5, etc.
- **Anthropic** - Claude 3.5 Sonnet, Claude 3 Opus, etc.
- **Google** - Gemini 1.5 Flash, Gemini 1.5 Pro
- **Ollama** - Local LLMs (Llama, Mistral, Phi, etc.)

## Using Built-in Providers

### OpenAI (Default)

```python
from react_agent_framework import ReactAgent

# Simple string (defaults to OpenAI)
agent = ReactAgent(
    name="Assistant",
    provider="gpt-4o-mini"
)

# Explicit URL-style
agent = ReactAgent(
    name="Assistant",
    provider="openai://gpt-4o-mini"
)

# With API key
agent = ReactAgent(
    name="Assistant",
    provider="gpt-4o-mini",
    api_key="sk-..."
)
```

### Anthropic Claude

```python
# URL-style
agent = ReactAgent(
    name="Claude Assistant",
    provider="anthropic://claude-3-5-sonnet-20241022"
)

# Auto-detected from model name
agent = ReactAgent(
    name="Claude Assistant",
    provider="claude-3-5-sonnet-20241022"
)

# Using provider object
from react_agent_framework.providers import AnthropicProvider

provider = AnthropicProvider(
    model="claude-3-5-sonnet-20241022",
    api_key="sk-ant-..."  # Optional, uses ANTHROPIC_API_KEY env var
)

agent = ReactAgent(name="Assistant", provider=provider)
```

### Google Gemini

```python
# URL-style
agent = ReactAgent(
    name="Gemini Assistant",
    provider="google://gemini-1.5-flash"
)

# Auto-detected from model name
agent = ReactAgent(
    name="Gemini Assistant",
    provider="gemini-1.5-flash"
)

# Using provider object
from react_agent_framework.providers import GoogleProvider

provider = GoogleProvider(
    model="gemini-1.5-flash",
    api_key="..."  # Optional, uses GOOGLE_API_KEY env var
)

agent = ReactAgent(name="Assistant", provider=provider)
```

### Ollama (Local LLMs)

```python
# URL-style (default localhost:11434)
agent = ReactAgent(
    name="Llama Assistant",
    provider="ollama://llama3.2"
)

# Auto-detected from model name
agent = ReactAgent(
    name="Llama Assistant",
    provider="llama3.2"  # Also works: mistral, phi, codellama
)

# Using provider object with custom URL
from react_agent_framework.providers import OllamaProvider

provider = OllamaProvider(
    model="llama3.2",
    base_url="http://localhost:11434"  # Custom Ollama server
)

agent = ReactAgent(name="Assistant", provider=provider)
```

!!! note "Ollama Setup"
    To use Ollama, you need to install and run it locally:
    ```bash
    # Install Ollama
    curl -fsSL https://ollama.ai/install.sh | sh

    # Pull a model
    ollama pull llama3.2

    # Start Ollama server
    ollama serve
    ```

## Provider Comparison

| Provider | Best For | API Key Required | Local | Cost |
|----------|----------|------------------|-------|------|
| **OpenAI** | General-purpose, latest models | Yes | No | $$ |
| **Anthropic** | Long context, analysis | Yes | No | $$ |
| **Google** | Fast, multimodal | Yes | No | $ |
| **Ollama** | Privacy, offline use | No | Yes | Free |

## Auto-Detection

The framework automatically detects the provider based on model name:

```python
from react_agent_framework import ReactAgent

# These are automatically detected:
agent1 = ReactAgent(provider="gpt-4o-mini")              # -> OpenAI
agent2 = ReactAgent(provider="claude-3-5-sonnet-20241022")  # -> Anthropic
agent3 = ReactAgent(provider="gemini-1.5-flash")         # -> Google
agent4 = ReactAgent(provider="llama3.2")                 # -> Ollama
agent5 = ReactAgent(provider="mistral")                  # -> Ollama

# Check what was detected
print(agent1.get_provider_info())
# Output: {'provider': 'OpenAIProvider', 'model': 'gpt-4o-mini'}
```

## Creating Custom Providers

To create a custom provider, extend `BaseLLMProvider`:

### Step 1: Define Provider Class

```python
from typing import List, Optional
from react_agent_framework.providers.base import BaseLLMProvider, Message

class CustomProvider(BaseLLMProvider):
    """Custom LLM provider"""

    def __init__(
        self,
        model: str,
        api_key: Optional[str] = None,
        base_url: str = "https://api.example.com",
        **kwargs
    ):
        """
        Initialize custom provider

        Args:
            model: Model identifier
            api_key: API key for authentication
            base_url: API base URL
            **kwargs: Additional provider-specific parameters
        """
        super().__init__(model, api_key, **kwargs)
        self.base_url = base_url

    def generate(
        self,
        messages: List[Message],
        temperature: float = 0,
        **kwargs
    ) -> str:
        """
        Generate response from messages

        Args:
            messages: Conversation messages
            temperature: Sampling temperature (0-1)
            **kwargs: Additional generation parameters

        Returns:
            Generated text response
        """
        # 1. Convert messages to API format
        api_messages = self._convert_messages(messages)

        # 2. Call API
        response = self._call_api(
            messages=api_messages,
            temperature=temperature,
            **kwargs
        )

        # 3. Extract and return text
        return self._extract_text(response)

    def get_model_name(self) -> str:
        """Return model identifier"""
        return self.model

    def _convert_messages(self, messages: List[Message]) -> list:
        """Convert Message objects to API format"""
        return [
            {"role": msg.role, "content": msg.content}
            for msg in messages
        ]

    def _call_api(self, messages: list, temperature: float, **kwargs) -> dict:
        """Call the LLM API"""
        import requests

        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            **kwargs
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        response = requests.post(
            f"{self.base_url}/chat/completions",
            json=payload,
            headers=headers,
            timeout=60
        )
        response.raise_for_status()

        return response.json()

    def _extract_text(self, response: dict) -> str:
        """Extract text from API response"""
        return response["choices"][0]["message"]["content"]
```

### Step 2: Use Custom Provider

```python
from react_agent_framework import ReactAgent

# Create custom provider instance
provider = CustomProvider(
    model="custom-model-v1",
    api_key="your-api-key",
    base_url="https://api.custom-llm.com"
)

# Use with ReactAgent
agent = ReactAgent(
    name="Custom Assistant",
    provider=provider
)

@agent.tool()
def search(query: str) -> str:
    """Search tool"""
    return f"Results for: {query}"

# Agent now uses your custom provider
answer = agent.run("What is AI?", verbose=True)
```

## Real-World Example: Hugging Face Provider

Here's a complete example implementing a Hugging Face Inference API provider:

```python
from typing import List, Optional
import requests
from react_agent_framework.providers.base import BaseLLMProvider, Message

class HuggingFaceProvider(BaseLLMProvider):
    """
    Hugging Face Inference API provider

    Supports models hosted on Hugging Face Inference API
    """

    def __init__(
        self,
        model: str = "meta-llama/Llama-3.2-3B-Instruct",
        api_key: Optional[str] = None,
        **kwargs
    ):
        """
        Initialize Hugging Face provider

        Args:
            model: Model ID on Hugging Face Hub
            api_key: Hugging Face API token (or use HF_TOKEN env var)
            **kwargs: Additional parameters
        """
        super().__init__(model, api_key, **kwargs)

        # Get API key from env if not provided
        if not self.api_key:
            import os
            self.api_key = os.getenv("HF_TOKEN")

        if not self.api_key:
            raise ValueError(
                "Hugging Face API token required. "
                "Set HF_TOKEN env var or pass api_key parameter"
            )

        self.base_url = "https://api-inference.huggingface.co/models"

    def generate(
        self,
        messages: List[Message],
        temperature: float = 0,
        max_tokens: int = 500,
        **kwargs
    ) -> str:
        """Generate response using HF Inference API"""

        # Build prompt from messages
        prompt = self._build_prompt(messages)

        # Prepare request
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {
            "inputs": prompt,
            "parameters": {
                "temperature": temperature,
                "max_new_tokens": max_tokens,
                "return_full_text": False,
                **kwargs
            }
        }

        try:
            response = requests.post(
                f"{self.base_url}/{self.model}",
                headers=headers,
                json=payload,
                timeout=60
            )
            response.raise_for_status()

            result = response.json()

            # Extract generated text
            if isinstance(result, list) and len(result) > 0:
                return result[0].get("generated_text", "")
            else:
                return str(result)

        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 503:
                raise RuntimeError(
                    f"Model '{self.model}' is loading. "
                    "Please wait a moment and try again."
                )
            raise RuntimeError(f"HF API error: {str(e)}")

    def _build_prompt(self, messages: List[Message]) -> str:
        """Build chat prompt from messages"""
        prompt_parts = []

        for msg in messages:
            if msg.role == "system":
                prompt_parts.append(f"System: {msg.content}")
            elif msg.role == "user":
                prompt_parts.append(f"User: {msg.content}")
            elif msg.role == "assistant":
                prompt_parts.append(f"Assistant: {msg.content}")

        prompt_parts.append("Assistant:")
        return "\n\n".join(prompt_parts)

    def get_model_name(self) -> str:
        """Return model name"""
        return self.model

# Usage
provider = HuggingFaceProvider(
    model="meta-llama/Llama-3.2-3B-Instruct",
    api_key="hf_..."
)

agent = ReactAgent(name="HF Assistant", provider=provider)
```

## Advanced: Streaming Support

Add streaming support to your custom provider:

```python
from typing import Iterator

class StreamingProvider(BaseLLMProvider):
    """Provider with streaming support"""

    def generate(self, messages: List[Message], temperature: float = 0, **kwargs) -> str:
        """Non-streaming generation (required)"""
        # Convert streaming to string
        chunks = list(self.generate_stream(messages, temperature, **kwargs))
        return "".join(chunks)

    def generate_stream(
        self,
        messages: List[Message],
        temperature: float = 0,
        **kwargs
    ) -> Iterator[str]:
        """
        Streaming generation (optional)

        Yields:
            Text chunks as they are generated
        """
        import requests

        payload = {
            "model": self.model,
            "messages": [{"role": m.role, "content": m.content} for m in messages],
            "temperature": temperature,
            "stream": True,
            **kwargs
        }

        headers = {"Authorization": f"Bearer {self.api_key}"}

        with requests.post(
            f"{self.base_url}/chat/completions",
            json=payload,
            headers=headers,
            stream=True,
            timeout=60
        ) as response:
            response.raise_for_status()

            for line in response.iter_lines():
                if line:
                    # Parse SSE format
                    if line.startswith(b"data: "):
                        data = line[6:].decode("utf-8")
                        if data == "[DONE]":
                            break

                        import json
                        chunk = json.loads(data)
                        delta = chunk["choices"][0]["delta"]

                        if "content" in delta:
                            yield delta["content"]

    def get_model_name(self) -> str:
        return self.model
```

## Error Handling Best Practices

Implement robust error handling:

```python
class RobustProvider(BaseLLMProvider):
    """Provider with comprehensive error handling"""

    def generate(self, messages: List[Message], temperature: float = 0, **kwargs) -> str:
        """Generate with error handling"""
        try:
            return self._generate_internal(messages, temperature, **kwargs)

        except requests.exceptions.ConnectionError:
            raise ConnectionError(
                f"Cannot connect to {self.base_url}. "
                "Check your internet connection."
            )

        except requests.exceptions.Timeout:
            raise TimeoutError(
                f"Request timed out for model '{self.model}'. "
                "Try again or use a different model."
            )

        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                raise PermissionError(
                    "Invalid API key. Check your credentials."
                )
            elif e.response.status_code == 429:
                raise RuntimeError(
                    "Rate limit exceeded. Please wait and try again."
                )
            elif e.response.status_code == 503:
                raise RuntimeError(
                    "Service temporarily unavailable. Try again later."
                )
            else:
                raise RuntimeError(
                    f"API error ({e.response.status_code}): {e.response.text}"
                )

        except Exception as e:
            raise RuntimeError(f"Unexpected error: {str(e)}")

    def _generate_internal(self, messages, temperature, **kwargs):
        """Internal generation logic"""
        # Implementation
        pass

    def get_model_name(self) -> str:
        return self.model
```

## Testing Your Provider

Test your custom provider:

```python
from react_agent_framework.providers.base import Message

def test_custom_provider():
    """Test custom provider implementation"""

    # Create provider
    provider = CustomProvider(
        model="test-model",
        api_key="test-key"
    )

    # Test basic generation
    messages = [
        Message(role="system", content="You are a helpful assistant."),
        Message(role="user", content="Hello!")
    ]

    try:
        response = provider.generate(messages, temperature=0.7)
        print(f"✅ Generation works: {response[:50]}...")

    except Exception as e:
        print(f"❌ Generation failed: {str(e)}")

    # Test with ReactAgent
    from react_agent_framework import ReactAgent

    agent = ReactAgent(name="Test Agent", provider=provider)

    @agent.tool()
    def dummy_tool(query: str) -> str:
        return f"Result: {query}"

    try:
        answer = agent.run("Test query", verbose=True)
        print(f"✅ Agent integration works: {answer[:50]}...")

    except Exception as e:
        print(f"❌ Agent integration failed: {str(e)}")

# Run tests
test_custom_provider()
```

## Provider Factory Integration

Optionally, integrate your provider into the factory:

```python
# In your custom module
from react_agent_framework.providers.factory import create_provider
from react_agent_framework.providers.base import BaseLLMProvider

# Save original factory function
_original_create = create_provider

def create_provider_with_custom(provider, api_key=None):
    """Extended factory with custom provider support"""

    if isinstance(provider, str):
        if provider.startswith("custom://"):
            model = provider.replace("custom://", "")
            from my_module import CustomProvider
            return CustomProvider(model=model, api_key=api_key)

    # Fall back to original
    return _original_create(provider, api_key)

# Monkey patch (use with caution)
import react_agent_framework.providers.factory as factory
factory.create_provider = create_provider_with_custom

# Now you can use:
# agent = ReactAgent(provider="custom://my-model")
```

## Best Practices

### 1. Handle Rate Limits

```python
import time
from functools import wraps

def retry_with_backoff(max_retries=3):
    """Decorator for retry logic"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except requests.exceptions.HTTPError as e:
                    if e.response.status_code == 429:
                        if attempt < max_retries - 1:
                            wait = 2 ** attempt
                            time.sleep(wait)
                            continue
                    raise
            return None
        return wrapper
    return decorator

class RateLimitedProvider(BaseLLMProvider):
    @retry_with_backoff(max_retries=3)
    def generate(self, messages, temperature=0, **kwargs):
        # Implementation
        pass
```

### 2. Validate Configuration

```python
class ValidatedProvider(BaseLLMProvider):
    def __init__(self, model: str, api_key: Optional[str] = None, **kwargs):
        super().__init__(model, api_key, **kwargs)

        # Validate API key
        if not self.api_key:
            raise ValueError("API key is required")

        # Validate model
        if not self._is_valid_model(model):
            raise ValueError(f"Invalid model: {model}")

    def _is_valid_model(self, model: str) -> bool:
        """Check if model is supported"""
        valid_models = ["model-a", "model-b", "model-c"]
        return model in valid_models
```

### 3. Add Logging

```python
import logging

logger = logging.getLogger(__name__)

class LoggedProvider(BaseLLMProvider):
    def generate(self, messages, temperature=0, **kwargs):
        logger.info(f"Generating with model {self.model}, temp={temperature}")

        try:
            response = self._call_api(messages, temperature, **kwargs)
            logger.info("Generation successful")
            return response

        except Exception as e:
            logger.error(f"Generation failed: {str(e)}")
            raise
```

## Next Steps

- [Basic Usage](../getting-started/basic-usage.md) - Learn agent basics
- [Built-in Tools](../features/built-in-tools.md) - Explore available tools
- [Custom Tools](custom-tools.md) - Create custom tools
- [Multi-Provider Example](../examples/multi-provider.md) - See all providers in action

## Further Reading

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Anthropic Claude API](https://docs.anthropic.com)
- [Google Gemini API](https://ai.google.dev/docs)
- [Ollama Documentation](https://ollama.ai/docs)
- [Hugging Face Inference API](https://huggingface.co/inference-api)
