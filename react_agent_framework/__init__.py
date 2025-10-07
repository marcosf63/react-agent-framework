"""
ReAct Agent Framework - Framework para criar agentes com raciocínio e ação
"""

__version__ = "0.1.0"
__author__ = "Marcos"
__description__ = "Framework genérico para criar aplicações com agentes AI usando padrão ReAct"

from react_agent_framework.core.agent import AgenteReAct
from react_agent_framework.core.base import Ferramenta, Pensamento, Acao, Observacao, AcaoTipo

__all__ = [
    "AgenteReAct",
    "Ferramenta",
    "Pensamento",
    "Acao",
    "Observacao",
    "AcaoTipo",
]
