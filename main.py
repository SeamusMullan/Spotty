import typer
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.panel import Panel
from rich import print as rprint
import pandas as pd
import time

app = typer.Typer(help="Spotty - Download your Spotify music from Exportify CSV files")
console = Console()


@app.command()
def version():
    """
    Show the version of Spotty.
    """
    version_text = (
        "[bold cyan]Spotty[/bold cyan] [dim]v0.1.0[/dim]\n"
        "A terminal app for downloading songs from Exportify CSV files.\n"
        "\n"
        "[dim]Made with ❤️  and Python[/dim]"
    )
    panel = Panel(version_text, border_style="cyan")
    console.print(panel)


def main():
    app()


if __name__ == "__main__":
    main()
