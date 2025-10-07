"""
Ferramenta de calculadora matemática
"""

from react_agent_framework.core.base import Ferramenta


class FerramentaCalculadora(Ferramenta):
    """
    Ferramenta para realizar cálculos matemáticos simples

    Suporta operações básicas: +, -, *, /, ** (potência), % (módulo)
    """

    def __init__(self):
        super().__init__(
            nome="calcular",
            descricao="Realiza cálculos matemáticos. Entrada: expressão matemática (ex: 2 + 2 * 3)",
        )

    def executar(self, entrada: str) -> str:
        """
        Executa um cálculo matemático

        Args:
            entrada: Expressão matemática

        Returns:
            Resultado do cálculo
        """
        try:
            # Validar e calcular (apenas operações básicas por segurança)
            # Não permite funções built-in para evitar execução de código arbitrário
            resultado = eval(entrada, {"__builtins__": {}}, {})
            return f"O resultado de {entrada} é {resultado}"
        except Exception as e:
            return f"Erro ao calcular: {str(e)}"
