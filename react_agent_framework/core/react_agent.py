"""
ReactAgent with multi-provider support
"""

from datetime import datetime
from typing import Callable, Dict, List, Optional, Any, Union
from functools import wraps
from dotenv import load_dotenv

from react_agent_framework.providers.base import BaseLLMProvider, Message
from react_agent_framework.providers.factory import create_provider

load_dotenv()


class ReactAgent:
    """
    ReAct Agent with FastAPI-style API and multi-provider support

    Example:
        ```python
        # OpenAI (default)
        agent = ReactAgent(
            name="Assistant",
            provider="gpt-4o-mini"
        )

        # Anthropic Claude
        agent = ReactAgent(
            name="Assistant",
            provider="anthropic://claude-3-5-sonnet-20241022"
        )

        # Google Gemini
        agent = ReactAgent(
            name="Assistant",
            provider="google://gemini-1.5-flash"
        )

        # Ollama (local)
        agent = ReactAgent(
            name="Assistant",
            provider="ollama://llama3.2"
        )

        @agent.tool()
        def search(query: str) -> str:
            '''Search the internet'''
            return results

        answer = agent.run("What is the capital of France?")
        ```
    """

    def __init__(
        self,
        name: str = "ReactAgent",
        description: str = "An intelligent ReAct agent",
        provider: Union[str, BaseLLMProvider] = "gpt-4o-mini",
        instructions: Optional[str] = None,
        temperature: float = 0,
        max_iterations: int = 10,
        api_key: Optional[str] = None,
        execution_date: Optional[datetime] = None,
    ):
        """
        Initialize ReactAgent

        Args:
            name: Agent name
            description: Agent description
            provider: LLM provider (string or BaseLLMProvider instance)
                     Examples: "gpt-4o-mini", "anthropic://claude-3-5-sonnet",
                              "google://gemini-1.5-flash", "ollama://llama3.2"
            instructions: Custom instructions for the agent
            temperature: Model temperature (0-1)
            max_iterations: Maximum iterations
            api_key: API key for the provider (uses env if not provided)
            execution_date: Execution date (uses now() if not provided)
        """
        self.name = name
        self.description = description
        self.temperature = temperature
        self.max_iterations = max_iterations
        self.execution_date = execution_date or datetime.now()

        # Create or use provider
        self.provider = create_provider(provider, api_key=api_key)

        self._tools: Dict[str, Callable] = {}
        self._tool_descriptions: Dict[str, str] = {}
        self.history: List[Dict[str, Any]] = []

        # Default instructions
        self._instructions = instructions or self._get_default_instructions()

    def _get_default_instructions(self) -> str:
        """Returns default agent instructions"""
        return f"""You are {self.name}.

Description: {self.description}

Execution date: {self.execution_date.strftime('%Y-%m-%d %H:%M:%S')}
Provider: {self.provider.get_model_name()}

You are a ReAct (Reasoning + Acting) agent that solves problems by alternating between thinking and acting."""

    def tool(self, name: Optional[str] = None, description: Optional[str] = None):
        """
        Decorator to register a tool

        Args:
            name: Tool name (uses function name if not provided)
            description: Tool description (uses docstring if not provided)

        Example:
            ```python
            @agent.tool()
            def search(query: str) -> str:
                '''Search information on the internet'''
                return search_function(query)
            ```
        """

        def decorator(func: Callable) -> Callable:
            tool_name = name or func.__name__
            tool_desc = description or func.__doc__ or "No description"

            self._tools[tool_name] = func
            self._tool_descriptions[tool_name] = tool_desc.strip()

            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            return wrapper

        return decorator

    def _create_system_prompt(self) -> str:
        """Creates system prompt with available tools"""
        tools_desc = "\n".join(
            [f"- {name}: {desc}" for name, desc in self._tool_descriptions.items()]
        )

        return f"""{self._instructions}

Available tools:
{tools_desc}

You must follow this format EXACTLY:

Thought: [your reasoning about what to do]
Action: [tool name]
Action Input: [input for the tool]

You will receive:
Observation: [action result]

Continue this cycle until you can answer. When you have the final answer, use:

Thought: [final reasoning]
Action: finish
Action Input: [your final answer]

IMPORTANT:
- Use EXACTLY the names "Thought:", "Action:", "Action Input:", "Observation:"
- Always start with a Thought
- Each action must have an input
- Use "finish" when you have the complete answer"""

    def _extract_thought_action(
        self, text: str
    ) -> tuple[Optional[str], Optional[str], Optional[str]]:
        """Extracts thought, action and input from text"""
        lines = text.strip().split("\n")
        thought = None
        action = None
        action_input = None

        for line in lines:
            line = line.strip()
            if line.startswith("Thought:"):
                thought = line.replace("Thought:", "").strip()
            elif line.startswith("Action:"):
                action = line.replace("Action:", "").strip()
            elif line.startswith("Action Input:"):
                action_input = line.replace("Action Input:", "").strip()

        return thought, action, action_input

    def run(self, query: str, verbose: bool = False) -> str:
        """
        Run the agent with a query

        Args:
            query: The question/task
            verbose: If True, shows reasoning process

        Returns:
            The agent's final answer
        """
        messages = [
            Message(role="system", content=self._create_system_prompt()),
            Message(role="user", content=query),
        ]

        for iteration in range(self.max_iterations):
            if verbose:
                print(f"\n{'='*60}")
                print(f"ITERATION {iteration + 1}")
                print(f"{'='*60}")

            # Call LLM via provider
            response_text = self.provider.generate(messages=messages, temperature=self.temperature)

            if verbose:
                print(f"\n{response_text}")

            # Extract thought, action and input
            thought, action, action_input = self._extract_thought_action(response_text)

            if not action:
                messages.append(Message(role="assistant", content=response_text))
                messages.append(
                    Message(
                        role="user",
                        content="Please provide an Action and Action Input following the specified format.",
                    )
                )
                continue

            # Add to messages
            messages.append(Message(role="assistant", content=response_text))

            # Check for finish
            if action.lower() == "finish":
                self.history.append(
                    {
                        "iteration": iteration + 1,
                        "thought": thought,
                        "action": action,
                        "final_answer": action_input,
                    }
                )
                return action_input or "No answer provided"

            # Execute tool
            if action in self._tools:
                observation = self._tools[action](action_input or "")

                if verbose:
                    obs_display = (
                        f"{observation[:200]}..." if len(observation) > 200 else observation
                    )
                    print(f"\nObservation: {obs_display}")

                messages.append(Message(role="user", content=f"Observation: {observation}"))

                self.history.append(
                    {
                        "iteration": iteration + 1,
                        "thought": thought,
                        "action": action,
                        "action_input": action_input,
                        "observation": observation,
                    }
                )
            else:
                error = (
                    f"Tool '{action}' not found. Available tools: {', '.join(self._tools.keys())}"
                )
                messages.append(Message(role="user", content=f"Observation: {error}"))

                if verbose:
                    print(f"\nObservation: {error}")

        return "Maximum number of iterations reached without conclusive answer."

    async def arun(self, query: str, verbose: bool = False) -> str:
        """
        Async version of run (future implementation)

        Args:
            query: The question/task
            verbose: If True, shows reasoning process

        Returns:
            The agent's final answer
        """
        # For now, just calls sync version
        # Future: implement with async providers
        return self.run(query, verbose)

    def clear_history(self) -> None:
        """Clears execution history"""
        self.history = []

    def get_tools(self) -> Dict[str, str]:
        """Returns dictionary with registered tools and their descriptions"""
        return self._tool_descriptions.copy()

    def get_provider_info(self) -> Dict[str, str]:
        """Returns information about the current provider"""
        return {
            "provider": self.provider.__class__.__name__,
            "model": self.provider.get_model_name(),
        }

    def __repr__(self) -> str:
        provider_info = self.get_provider_info()
        return f"ReactAgent(name='{self.name}', provider={provider_info['provider']}, model='{provider_info['model']}', tools={len(self._tools)})"
