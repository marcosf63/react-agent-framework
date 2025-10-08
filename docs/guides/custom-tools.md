# Creating Custom Tools

Learn how to create powerful custom tools for your agents using decorators.

---

## Overview

Custom tools allow you to extend your agent's capabilities with any functionality you need. Tools are registered using the `@agent.tool()` decorator.

```python
from react_agent_framework import ReactAgent

agent = ReactAgent(name="Assistant")

@agent.tool()
def my_custom_tool(input: str) -> str:
    """Tool description that the LLM will see"""
    # Your implementation
    return result
```

---

## Basic Tool Creation

### Simple Tool

```python
from react_agent_framework import ReactAgent

agent = ReactAgent(name="Assistant")

@agent.tool()
def get_current_time() -> str:
    """Get the current time"""
    from datetime import datetime
    now = datetime.now()
    return f"Current time: {now.strftime('%H:%M:%S')}"

# Agent can now use this tool
answer = agent.run("What time is it?")
```

### Tool with Parameters

```python
@agent.tool()
def greet(name: str) -> str:
    """Greet someone by name"""
    return f"Hello, {name}! Nice to meet you!"

answer = agent.run("Greet Alice")
# Output: "Hello, Alice! Nice to meet you!"
```

---

## Custom Name and Description

Override the tool name and description:

```python
@agent.tool(
    name="temperature_converter",
    description="Convert temperature between Celsius and Fahrenheit"
)
def convert_temp(input_str: str) -> str:
    """Internal function docstring"""
    # Parse input like "25 C to F" or "77 F to C"
    # ... implementation ...
    return result
```

---

## Type Hints and Validation

Use type hints for better LLM understanding:

```python
@agent.tool()
def calculate_area(length: float, width: float) -> str:
    """
    Calculate the area of a rectangle.

    Args:
        length: Length in meters
        width: Width in meters

    Returns:
        Area in square meters
    """
    area = length * width
    return f"Area: {area} m²"
```

---

## Error Handling

Always handle errors gracefully:

```python
@agent.tool()
def divide_numbers(expression: str) -> str:
    """Divide two numbers. Format: 'a / b'"""
    try:
        parts = expression.split("/")
        a = float(parts[0].strip())
        b = float(parts[1].strip())

        if b == 0:
            return "Error: Cannot divide by zero"

        result = a / b
        return f"{a} / {b} = {result}"

    except (ValueError, IndexError) as e:
        return f"Error: Invalid format. Use 'number / number'"
    except Exception as e:
        return f"Error: {str(e)}"
```

---

## Complete Example

Personal assistant with multiple custom tools:

```python
from react_agent_framework import ReactAgent
from datetime import datetime
import random

agent = ReactAgent(
    name="Personal Assistant",
    provider="gpt-4o-mini"
)

@agent.tool()
def get_datetime() -> str:
    """Get current date and time"""
    now = datetime.now()
    return f"Date: {now.strftime('%Y-%m-%d')}, Time: {now.strftime('%H:%M:%S')}"

@agent.tool()
def random_number(range_str: str) -> str:
    """Generate random number. Format: 'min-max' (e.g., '1-100')"""
    try:
        min_val, max_val = map(int, range_str.split("-"))
        number = random.randint(min_val, max_val)
        return f"Random number between {min_val} and {max_val}: {number}"
    except Exception as e:
        return f"Error: Use format 'min-max' (e.g., '1-100')"

@agent.tool()
def convert_temperature(input_str: str) -> str:
    """Convert temperature. Format: 'C to F: 25' or 'F to C: 77'"""
    try:
        if "C to F" in input_str.upper():
            celsius = float(input_str.split(":")[-1].strip())
            fahrenheit = (celsius * 9/5) + 32
            return f"{celsius}°C = {fahrenheit}°F"
        elif "F to C" in input_str.upper():
            fahrenheit = float(input_str.split(":")[-1].strip())
            celsius = (fahrenheit - 32) * 5/9
            return f"{fahrenheit}°F = {celsius:.2f}°C"
        else:
            return "Use format: 'C to F: value' or 'F to C: value'"
    except Exception as e:
        return f"Conversion error: {str(e)}"

# Use the tools
answer = agent.run("What time is it?")
answer = agent.run("Generate a random number between 1 and 100")
answer = agent.run("Convert 25 Celsius to Fahrenheit")
```

---

## Advanced Patterns

### Tool with External API

```python
import requests

@agent.tool()
def get_weather(city: str) -> str:
    """Get current weather for a city"""
    try:
        # Example with a weather API
        api_key = "your_api_key"
        url = f"https://api.weather.com/v1/current?city={city}&key={api_key}"

        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()
        temp = data.get("temperature")
        condition = data.get("condition")

        return f"Weather in {city}: {temp}°C, {condition}"

    except requests.RequestException as e:
        return f"Error fetching weather: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"
```

### Tool with State

```python
class DatabaseTool:
    def __init__(self):
        self.cache = {}

    def create_tool(self, agent):
        @agent.tool()
        def query_database(query: str) -> str:
            """Query the database"""
            # Check cache
            if query in self.cache:
                return f"Cached: {self.cache[query]}"

            # Simulate database query
            result = f"Result for: {query}"
            self.cache[query] = result
            return result

        return query_database

# Usage
agent = ReactAgent(name="DB Agent")
db_tool = DatabaseTool()
db_tool.create_tool(agent)
```

### Async Tool (Future Support)

```python
import asyncio

@agent.tool()
def fetch_data(url: str) -> str:
    """Fetch data from URL"""
    # For now, use sync wrapper
    async def _fetch():
        # async implementation
        pass

    # Run in event loop
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(_fetch())
    return result
```

---

## Best Practices

### 1. Clear Docstrings

The LLM uses docstrings to understand when to use your tool:

```python
# ✅ Good - clear and specific
@agent.tool()
def send_email(recipient: str, subject: str, body: str) -> str:
    """
    Send an email to a recipient.

    Args:
        recipient: Email address
        subject: Email subject line
        body: Email message content

    Returns:
        Success or error message
    """
    # Implementation
    pass

# ❌ Bad - vague
@agent.tool()
def send_email(recipient: str, subject: str, body: str) -> str:
    """Send email"""
    pass
```

### 2. Always Return Strings

Tools should return strings for the LLM to interpret:

```python
# ✅ Good
@agent.tool()
def calculate(expression: str) -> str:
    result = eval(expression)
    return f"Result: {result}"

# ❌ Bad - returns number
@agent.tool()
def calculate(expression: str) -> float:
    return eval(expression)  # LLM expects string!
```

### 3. Handle All Errors

Never let exceptions crash the agent:

```python
@agent.tool()
def risky_operation(input: str) -> str:
    """Perform a risky operation"""
    try:
        # Risky code
        result = perform_operation(input)
        return f"Success: {result}"

    except ValueError as e:
        return f"Validation error: {str(e)}"
    except ConnectionError as e:
        return f"Connection failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"
```

### 4. Use Type Hints

```python
from typing import List, Dict, Optional

@agent.tool()
def process_data(
    items: str,  # Tools receive strings from LLM
    operation: str
) -> str:
    """Process a list of items"""
    # Parse string input
    item_list = items.split(",")

    # Type hints help with internal logic
    results: List[str] = []

    for item in item_list:
        # Process each item
        results.append(f"Processed: {item}")

    return ", ".join(results)
```

### 5. Descriptive Tool Names

```python
# ✅ Good - clear purpose
@agent.tool(name="convert_celsius_to_fahrenheit")
def convert_temp(celsius: str) -> str:
    pass

# ❌ Bad - vague
@agent.tool(name="convert")
def convert_temp(celsius: str) -> str:
    pass
```

### 6. Input Validation

```python
@agent.tool()
def book_flight(details: str) -> str:
    """Book a flight. Format: 'FROM to TO on DATE'"""
    try:
        # Parse and validate
        parts = details.split()
        if len(parts) != 5 or parts[1].lower() != "to" or parts[3].lower() != "on":
            return "Invalid format. Use: 'FROM to TO on DATE'"

        origin = parts[0]
        destination = parts[2]
        date = parts[4]

        # Validate date format
        from datetime import datetime
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            return "Invalid date. Use YYYY-MM-DD format"

        # Book flight
        return f"Flight booked: {origin} → {destination} on {date}"

    except Exception as e:
        return f"Booking error: {str(e)}"
```

---

## Testing Your Tools

Test tools independently before using with agents:

```python
# Create agent and tool
agent = ReactAgent(name="Test Agent")

@agent.tool()
def my_tool(input: str) -> str:
    """Test tool"""
    return f"Processed: {input}"

# Test directly
result = my_tool("test input")
print(result)  # "Processed: test input"

# Test with agent
answer = agent.run("Use my_tool with input 'hello'")
print(answer)
```

---

## Common Patterns

### Data Fetcher

```python
@agent.tool()
def fetch_user_data(user_id: str) -> str:
    """Get user information by ID"""
    # Fetch from database/API
    user = get_user_from_db(user_id)
    return f"User {user_id}: {user.name}, {user.email}"
```

### Calculator

```python
@agent.tool()
def calculate(expression: str) -> str:
    """Evaluate mathematical expression"""
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return f"{expression} = {result}"
    except:
        return "Invalid expression"
```

### Formatter

```python
@agent.tool()
def format_json(data: str) -> str:
    """Format JSON data"""
    import json
    try:
        obj = json.loads(data)
        formatted = json.dumps(obj, indent=2)
        return formatted
    except:
        return "Invalid JSON"
```

---

## Next Steps

<div class="grid cards" markdown>

-   :material-package: __Use Built-in Tools__

    ---

    Explore available built-in tools

    [:octicons-arrow-right-24: Built-in Tools](../features/built-in-tools.md)

-   :material-connection: __MCP Integration__

    ---

    Connect to external tool servers

    [:octicons-arrow-right-24: MCP Integration](../features/mcp-integration.md)

-   :material-code: __Examples__

    ---

    See complete examples

    [:octicons-arrow-right-24: Custom Tools Example](https://github.com/marcosf63/react-agent-framework/blob/main/react_agent_framework/examples/custom_tools.py)

</div>
