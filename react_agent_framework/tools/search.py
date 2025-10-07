"""
Ferramenta de pesquisa na internet
"""

from react_agent_framework.core.base import Ferramenta
from duckduckgo_search import DDGS


class FerramentaPesquisa(Ferramenta):
    """
    Ferramenta para pesquisar informações na internet usando DuckDuckGo

    Esta ferramenta não requer API key e fornece resultados de pesquisa
    de forma gratuita e anônima.
    """

    def __init__(self, max_resultados: int = 5):
        """
        Inicializa a ferramenta de pesquisa

        Args:
            max_resultados: Número máximo de resultados a retornar (padrão: 5)
        """
        super().__init__(
            nome="pesquisar",
            descricao="Pesquisa informações na internet. Entrada: a consulta de pesquisa",
        )
        self.max_resultados = max_resultados

    def executar(self, entrada: str) -> str:
        """
        Executa uma pesquisa na internet

        Args:
            entrada: A consulta de pesquisa

        Returns:
            Resultados da pesquisa formatados
        """
        try:
            with DDGS() as ddgs:
                resultados = list(ddgs.text(entrada, max_results=self.max_resultados))

            if not resultados:
                return "Nenhum resultado encontrado."

            # Formatar resultados
            texto_formatado = []
            for i, resultado in enumerate(resultados, 1):
                texto_formatado.append(
                    f"{i}. {resultado['title']}\n"
                    f"   {resultado['body']}\n"
                    f"   URL: {resultado['href']}"
                )

            return "\n\n".join(texto_formatado)

        except Exception as e:
            return f"Erro ao pesquisar: {str(e)}"
