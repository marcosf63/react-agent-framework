"""
Exemplo básico de uso do ReAct Agent Framework
"""

from react_agent_framework import AgenteReAct
from react_agent_framework.tools import FerramentaPesquisa, FerramentaCalculadora


def main():
    # Criar ferramentas
    ferramentas = [FerramentaPesquisa(), FerramentaCalculadora()]

    # Criar agente
    agente = AgenteReAct(ferramentas=ferramentas, modelo="gpt-4o-mini", max_iteracoes=10)

    # Fazer uma pergunta
    print("=" * 80)
    print("EXEMPLO BÁSICO - ReAct Agent Framework")
    print("=" * 80)

    pergunta = "Qual é a capital da França e quantos habitantes tem aproximadamente?"

    print(f"\nPergunta: {pergunta}\n")

    resposta = agente.executar(pergunta, verbose=True)

    print("\n" + "=" * 80)
    print(f"RESPOSTA FINAL: {resposta}")
    print("=" * 80)


if __name__ == "__main__":
    main()
