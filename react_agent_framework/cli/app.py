#!/usr/bin/env python
"""
CLI do ReAct Agent Framework usando Typer
"""
import typer
from rich.console import Console
from rich.panel import Panel

from react_agent_framework import AgenteReAct, __version__
from react_agent_framework.tools import FerramentaPesquisa, FerramentaCalculadora

app = typer.Typer(
    name="react-agent",
    help="ReAct Agent Framework - CLI para criar agentes com raciocínio e ação",
    add_completion=False,
)
console = Console()


@app.command()
def perguntar(
    pergunta: str = typer.Argument(..., help="A pergunta que você deseja fazer ao agente"),
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Mostrar o raciocínio passo a passo do agente"
    ),
    modelo: str = typer.Option(
        "gpt-4o-mini", "--modelo", "-m", help="Modelo da OpenAI a usar (gpt-4o-mini, gpt-4, etc)"
    ),
    max_iteracoes: int = typer.Option(
        10, "--max-iteracoes", "-i", help="Número máximo de iterações do agente"
    ),
):
    """
    Faz uma pergunta ao agente ReAct e recebe uma resposta
    """
    try:
        # Criar ferramentas
        ferramentas = [FerramentaPesquisa(), FerramentaCalculadora()]

        # Criar agente
        agente = AgenteReAct(ferramentas=ferramentas, modelo=modelo, max_iteracoes=max_iteracoes)

        # Mostrar pergunta
        console.print()
        console.print(
            Panel(f"[bold cyan]{pergunta}[/bold cyan]", title="🤔 Pergunta", border_style="cyan")
        )

        # Executar agente
        if not verbose:
            with console.status("[bold green]Processando...", spinner="dots"):
                resposta = agente.executar(pergunta, verbose=False)
        else:
            console.print("\n[bold yellow]⚙️  Processamento (modo verbose)[/bold yellow]\n")
            resposta = agente.executar(pergunta, verbose=True)

        # Mostrar resposta final
        console.print()
        console.print(
            Panel(
                f"[bold green]{resposta}[/bold green]",
                title="✅ Resposta Final",
                border_style="green",
            )
        )
        console.print()

    except KeyboardInterrupt:
        console.print("\n[yellow]Operação cancelada pelo usuário[/yellow]")
        raise typer.Exit(0)
    except Exception as e:
        console.print(f"\n[bold red]❌ Erro:[/bold red] {str(e)}")
        raise typer.Exit(1)


@app.command()
def interativo(
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Mostrar o raciocínio passo a passo do agente"
    ),
    modelo: str = typer.Option("gpt-4o-mini", "--modelo", "-m", help="Modelo da OpenAI a usar"),
):
    """
    Modo interativo - faça múltiplas perguntas em sequência
    """
    console.print()
    console.print(
        Panel(
            "[bold cyan]Modo Interativo do ReAct Agent Framework[/bold cyan]\n\n"
            "Digite suas perguntas ou 'sair' para encerrar.\n"
            f"Modo verbose: [yellow]{'Ativado' if verbose else 'Desativado'}[/yellow]\n"
            f"Modelo: [yellow]{modelo}[/yellow]",
            title="🤖 ReAct Agent",
            border_style="cyan",
        )
    )
    console.print()

    # Criar ferramentas uma vez
    ferramentas = [FerramentaPesquisa(), FerramentaCalculadora()]

    while True:
        try:
            # Pedir pergunta
            pergunta = console.input("[bold cyan]❓ Pergunta:[/bold cyan] ")

            if pergunta.lower() in ["sair", "exit", "quit", "q"]:
                console.print("\n[yellow]👋 Até logo![/yellow]\n")
                break

            if not pergunta.strip():
                continue

            # Criar novo agente para cada pergunta
            agente = AgenteReAct(ferramentas=ferramentas, modelo=modelo, max_iteracoes=10)

            # Executar
            if not verbose:
                with console.status("[bold green]Processando...", spinner="dots"):
                    resposta = agente.executar(pergunta, verbose=False)
            else:
                console.print("\n[bold yellow]⚙️  Processamento:[/bold yellow]\n")
                resposta = agente.executar(pergunta, verbose=True)

            # Mostrar resposta
            console.print()
            console.print(
                Panel(
                    f"[bold green]{resposta}[/bold green]",
                    title="✅ Resposta",
                    border_style="green",
                )
            )
            console.print()

        except KeyboardInterrupt:
            console.print("\n[yellow]👋 Até logo![/yellow]\n")
            break
        except Exception as e:
            console.print(f"\n[bold red]❌ Erro:[/bold red] {str(e)}\n")


@app.command()
def versao():
    """
    Mostra a versão do framework
    """
    console.print()
    console.print(
        Panel(
            "[bold cyan]ReAct Agent Framework[/bold cyan]\n"
            f"Versão: [yellow]{__version__}[/yellow]\n"
            "Modelo padrão: [yellow]gpt-4o-mini[/yellow]",
            title="📋 Versão",
            border_style="cyan",
        )
    )
    console.print()


def main():
    """Entry point do CLI"""
    app()


if __name__ == "__main__":
    main()
