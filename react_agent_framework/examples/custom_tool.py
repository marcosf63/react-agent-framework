"""
Exemplo de como criar uma ferramenta personalizada
"""

from react_agent_framework import AgenteReAct, Ferramenta
from react_agent_framework.tools import FerramentaPesquisa
import datetime


class FerramentaData(Ferramenta):
    """Ferramenta personalizada que retorna a data e hora atual"""

    def __init__(self):
        super().__init__(
            nome="data_hora", descricao="Retorna a data e hora atual. Não requer entrada."
        )

    def executar(self, entrada: str) -> str:
        agora = datetime.datetime.now()
        return f"Data: {agora.strftime('%d/%m/%Y')}, Hora: {agora.strftime('%H:%M:%S')}"


class FerramentaConversaoTemperatura(Ferramenta):
    """Ferramenta para converter temperaturas entre Celsius e Fahrenheit"""

    def __init__(self):
        super().__init__(
            nome="converter_temperatura",
            descricao="Converte temperatura. Entrada: 'C para F: 25' ou 'F para C: 77'",
        )

    def executar(self, entrada: str) -> str:
        try:
            entrada = entrada.strip()

            if "C para F" in entrada or "c para f" in entrada:
                # Extrair número
                celsius = float(entrada.split(":")[-1].strip())
                fahrenheit = (celsius * 9 / 5) + 32
                return f"{celsius}°C = {fahrenheit}°F"

            elif "F para C" in entrada or "f para c" in entrada:
                # Extrair número
                fahrenheit = float(entrada.split(":")[-1].strip())
                celsius = (fahrenheit - 32) * 5 / 9
                return f"{fahrenheit}°F = {celsius:.2f}°C"

            else:
                return "Formato inválido. Use 'C para F: valor' ou 'F para C: valor'"

        except Exception as e:
            return f"Erro ao converter: {str(e)}"


def main():
    # Criar ferramentas (built-in + personalizadas)
    ferramentas = [FerramentaPesquisa(), FerramentaData(), FerramentaConversaoTemperatura()]

    # Criar agente
    agente = AgenteReAct(ferramentas=ferramentas, modelo="gpt-4o-mini", max_iteracoes=10)

    print("=" * 80)
    print("EXEMPLO - Ferramentas Personalizadas")
    print("=" * 80)

    perguntas = [
        "Que horas são agora?",
        "Converta 25 graus Celsius para Fahrenheit",
        "Quanto é 100°F em Celsius?",
    ]

    for pergunta in perguntas:
        print(f"\n{'#'*80}")
        print(f"Pergunta: {pergunta}")
        print(f"{'#'*80}\n")

        resposta = agente.executar(pergunta, verbose=True)

        print(f"\n{'='*80}")
        print(f"RESPOSTA: {resposta}")
        print(f"{'='*80}\n")


if __name__ == "__main__":
    main()
