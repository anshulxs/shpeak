import json
from shpeak.llm import cmd_suggest, ps_suggest
from rich.console import Console
import re
import pyperclip

console = Console()

def cmd(query: str, verbose: bool, test: bool=False):
    result = cmd_suggest(query, verbose, test)
    if test:
        print(json.dumps(result, indent=4))

    console.print()
    console.print(f"[bold]OUERY: {result["intent"]}[/]")
    if not result["available"]:
        console.print(f"[bold magenta]{result["error"]}[/]")
    else:
        pyperclip.copy(result["command"])
        console.print()
        if result["irreversible"]:
            console.print(f"[bold underline bright_white]COMMAND[/] -> [cyan]{result["command"]}[/] [red1](WARNING)[/]")
        else:
            console.print(f"[bold underline bright_white]COMMAND[/] -> [cyan]{result["command"]}[/]")

        if verbose:
            console.print()
            console.print("[bold blue]Breakdown: [/]")
            console.print(f"[bold] • Cmdlet:[/] {result["breakdown"]["command"]}")
            console.print(f"[bold] • Description:[/]")
            description = re.split(r'(?<!\bDr)(?<!\bMr)(?<!\bMrs)(?<=[\.\!\?])\s+', result["breakdown"]["description"])
            console.print(*(f"    - {i}" for i in description), sep="\n")
            console.print(f"[bold] • Parameters:[/]")
            parameters = re.split(r'(?<!\bDr)(?<!\bMr)(?<!\bMrs)(?<=[\.\!\?])\s+', result["breakdown"]["parameters"])
            console.print(*(f"    - {i}" for i in parameters), sep="\n")
            console.print(f"[bold] • Output:[/] {result["breakdown"]["expected_output"]}")

            if result["safer"]:
                if result["safer"]["command"] and result["safer"]["command"]:
                    console.print()
                    console.print("[bold green]Safer alternative: [/]")
                    console.print(f" • [bold]Command:[/] {result["safer"]["command"]}")
                    console.print(f" • [bold]Why?[/] {result["safer"]["explanation"]}")

        if result["irreversible"]:
                    console.print()
                    console.print("[red1]WARNING:[/] [bold]THIS ACTION IS IRREVERSIBLE.[/]")
                    console.print(result["warning"]["description"])
                    console.print()
                    console.print("[bold yellow]BEFORE CONTINUING:[/]")
                    precautions = re.split(r'(?<!\bDr)(?<!\bMr)(?<!\bMrs)(?<=[\.\!\?])\s+', result["warning"]["precaution"])
                    console.print(*(f" • {i}" for i in precautions), sep="\n")
        console.print()


def ps(query: str, verbose: bool, test: bool=False):
    result = ps_suggest(query, verbose, test)
    if test:
        print(json.dumps(result, indent=4))

    console.print()
    console.print(f"[bold]OUERY: {result["intent"]}[/]")
    if not result["available"]:
        console.print(f"[bold magenta]{result["error"]}[/]")
    else:
        pyperclip.copy(result["command"])
        console.print()
        if result["irreversible"]:
            console.print(f"[bold underline bright_white]COMMAND[/] -> [cyan]{result["command"]}[/] [red1](WARNING)[/]")
        else:
            console.print(f"[bold underline bright_white]COMMAND[/] -> [cyan]{result["command"]}[/]")

        if verbose:
            console.print()
            console.print("[bold blue]Breakdown: [/]")
            console.print(f"[bold] • Cmdlet:[/] {result["breakdown"]["command"]}")
            console.print(f"[bold] • Description:[/]")
            description = re.split(r'(?<!\bDr)(?<!\bMr)(?<!\bMrs)(?<=[\.\!\?])\s+', result["breakdown"]["description"])
            console.print(*(f"    - {i}" for i in description), sep="\n")
            console.print(f"[bold] • Parameters:[/]")
            if isinstance(result["breakdown"]["parameters"], dict):
                 for k, v in result["breakdown"]["parameters"].items():
                      console.print(f"    - {k}: {v}")
            else:
                parameters = re.split(r'(?<!\bDr)(?<!\bMr)(?<!\bMrs)(?<=[\.\!\?])\s+', result["breakdown"]["parameters"])
                console.print(*(f"    • {i}" for i in parameters), sep="\n")
            console.print(f"[bold] • Output:[/] {result["breakdown"]["expected_output"]}")

            if result["safer"]:
                if result["safer"]["command"] and result["safer"]["command"]:
                    console.print()
                    console.print("[bold green]Safer alternative: [/]")
                    console.print(f" • [bold]Command:[/] {result["safer"]["command"]}")
                    console.print(f" • [bold]Why?[/] {result["safer"]["explanation"]}")

        if result["irreversible"]:
                    console.print()
                    console.print("[red1]WARNING:[/] [bold]THIS ACTION IS IRREVERSIBLE.[/]")
                    console.print(result["warning"]["description"])
                    console.print()
                    console.print("[bold yellow]BEFORE CONTINUING:[/]")
                    precautions = re.split(r'(?<!\bDr)(?<!\bMr)(?<!\bMrs)(?<=[\.\!\?])\s+', result["warning"]["precaution"])
                    console.print(*(f" • {i}" for i in precautions), sep="\n")
        console.print()