"""
Classes base do framework ReAct Agent
"""

from dataclasses import dataclass
from enum import Enum


class AcaoTipo(Enum):
    """Tipos de ação disponíveis"""

    PESQUISAR = "pesquisar"
    CALCULAR = "calcular"
    FINALIZAR = "finalizar"


@dataclass
class Pensamento:
    """Representa um pensamento do agente"""

    conteudo: str


@dataclass
class Acao:
    """Representa uma ação do agente"""

    tipo: AcaoTipo
    entrada: str


@dataclass
class Observacao:
    """Representa uma observação resultante de uma ação"""

    conteudo: str


class Ferramenta:
    """Classe base para ferramentas que podem ser usadas pelo agente"""

    def __init__(self, nome: str, descricao: str):
        """
        Inicializa uma ferramenta

        Args:
            nome: Nome identificador da ferramenta
            descricao: Descrição do que a ferramenta faz
        """
        self.nome = nome
        self.descricao = descricao

    def executar(self, entrada: str) -> str:
        """
        Executa a ferramenta com a entrada fornecida

        Args:
            entrada: Entrada para a ferramenta

        Returns:
            Resultado da execução

        Raises:
            NotImplementedError: Deve ser implementado pelas subclasses
        """
        raise NotImplementedError("Subclasses devem implementar o método executar")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(nome='{self.nome}')"
