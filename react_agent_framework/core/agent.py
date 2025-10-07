"""
Implementação do Agente ReAct
"""

import os
from typing import List, Dict, Any, Optional
import openai
from dotenv import load_dotenv

from react_agent_framework.core.base import Ferramenta

load_dotenv()


class AgenteReAct:
    """
    Agente ReAct que alterna entre Raciocínio (Reasoning) e Ação (Acting)

    Este agente usa o padrão ReAct para resolver problemas de forma autônoma,
    alternando entre pensamento, ação e observação até encontrar uma solução.
    """

    def __init__(
        self,
        ferramentas: List[Ferramenta],
        modelo: str = "gpt-4o-mini",
        max_iteracoes: int = 10,
        api_key: Optional[str] = None,
    ):
        """
        Inicializa o agente ReAct

        Args:
            ferramentas: Lista de ferramentas disponíveis para o agente
            modelo: Modelo da OpenAI a usar (padrão: gpt-4o-mini)
            max_iteracoes: Número máximo de iterações (padrão: 10)
            api_key: Chave da API OpenAI (opcional, usa variável de ambiente se não fornecida)
        """
        self.ferramentas = {f.nome: f for f in ferramentas}
        self.modelo = modelo
        self.max_iteracoes = max_iteracoes
        self.client = openai.OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))
        self.historico: List[Dict[str, Any]] = []

    def _criar_prompt_sistema(self) -> str:
        """Cria o prompt de sistema com as ferramentas disponíveis"""
        ferramentas_desc = "\n".join(
            [f"- {nome}: {f.descricao}" for nome, f in self.ferramentas.items()]
        )

        return f"""Você é um agente ReAct (Reasoning + Acting) que resolve problemas alternando entre pensamento e ação.

Ferramentas disponíveis:
{ferramentas_desc}

Você deve seguir este formato EXATAMENTE:

Pensamento: [seu raciocínio sobre o que fazer]
Ação: [nome da ferramenta]
Entrada da Ação: [entrada para a ferramenta]

Você receberá:
Observação: [resultado da ação]

Continue esse ciclo até poder responder. Quando tiver a resposta final, use:

Pensamento: [raciocínio final]
Ação: finalizar
Entrada da Ação: [sua resposta final]

IMPORTANTE:
- Use EXATAMENTE os nomes "Pensamento:", "Ação:", "Entrada da Ação:", "Observação:"
- Sempre comece com um Pensamento
- Cada ação deve ter uma entrada
- Use "finalizar" quando tiver a resposta completa"""

    def _extrair_pensamento_acao(
        self, texto: str
    ) -> tuple[Optional[str], Optional[str], Optional[str]]:
        """Extrai pensamento, ação e entrada do texto do LLM"""
        linhas = texto.strip().split("\n")
        pensamento = None
        acao = None
        entrada = None

        for linha in linhas:
            linha = linha.strip()
            if linha.startswith("Pensamento:"):
                pensamento = linha.replace("Pensamento:", "").strip()
            elif linha.startswith("Ação:"):
                acao = linha.replace("Ação:", "").strip()
            elif linha.startswith("Entrada da Ação:"):
                entrada = linha.replace("Entrada da Ação:", "").strip()

        return pensamento, acao, entrada

    def executar(self, pergunta: str, verbose: bool = True) -> str:
        """
        Executa o loop ReAct para responder a pergunta

        Args:
            pergunta: A pergunta/tarefa a ser resolvida
            verbose: Se True, imprime o raciocínio passo a passo

        Returns:
            A resposta final do agente
        """
        mensagens: List[Dict[str, str]] = [
            {"role": "system", "content": self._criar_prompt_sistema()},
            {"role": "user", "content": pergunta},
        ]

        for iteracao in range(self.max_iteracoes):
            if verbose:
                print(f"\n{'='*60}")
                print(f"ITERAÇÃO {iteracao + 1}")
                print(f"{'='*60}")

            # Obter resposta do LLM
            resposta = self.client.chat.completions.create(
                model=self.modelo, messages=mensagens, temperature=0  # type: ignore
            )

            resposta_texto = resposta.choices[0].message.content or ""

            if verbose:
                print(f"\n{resposta_texto}")

            # Extrair pensamento, ação e entrada
            pensamento, acao, entrada = self._extrair_pensamento_acao(resposta_texto)

            if not acao:
                mensagens.append({"role": "assistant", "content": resposta_texto})
                mensagens.append(
                    {
                        "role": "user",
                        "content": "Por favor, forneça uma Ação e Entrada da Ação seguindo o formato especificado.",
                    }
                )
                continue

            # Adicionar resposta ao histórico
            mensagens.append({"role": "assistant", "content": resposta_texto})

            # Verificar se deve finalizar
            if acao.lower() == "finalizar":
                self.historico.append(
                    {
                        "iteracao": iteracao + 1,
                        "pensamento": pensamento,
                        "acao": acao,
                        "resposta_final": entrada,
                    }
                )
                return entrada or "Resposta não fornecida"

            # Executar ação
            if acao in self.ferramentas:
                observacao = self.ferramentas[acao].executar(entrada or "")

                if verbose:
                    print(
                        f"\nObservação: {observacao[:200]}..."
                        if len(observacao) > 200
                        else f"\nObservação: {observacao}"
                    )

                # Adicionar observação ao histórico de mensagens
                mensagens.append({"role": "user", "content": f"Observação: {observacao}"})

                self.historico.append(
                    {
                        "iteracao": iteracao + 1,
                        "pensamento": pensamento,
                        "acao": acao,
                        "entrada": entrada,
                        "observacao": observacao,
                    }
                )
            else:
                erro = f"Ferramenta '{acao}' não encontrada. Ferramentas disponíveis: {', '.join(self.ferramentas.keys())}"
                mensagens.append({"role": "user", "content": f"Observação: {erro}"})

                if verbose:
                    print(f"\nObservação: {erro}")

        return "Número máximo de iterações atingido sem resposta conclusiva."

    def limpar_historico(self) -> None:
        """Limpa o histórico de execuções"""
        self.historico = []

    def obter_historico(self) -> List[Dict[str, Any]]:
        """
        Retorna o histórico de execuções

        Returns:
            Lista com o histórico de todas as iterações
        """
        return self.historico.copy()
